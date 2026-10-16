"""Validate the index locally; no network or executable mod loading required."""
import json
from pathlib import Path
from urllib.parse import urlparse
from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parent
index = json.loads((root / "index.json").read_text(encoding="utf-8"))
schema = json.loads((root / "schema/registry-v1.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(schema)
Draft202012Validator(schema).validate(index)
ids, packages = set(), set()
for mod in index["mods"]:
    assert mod["id"] not in ids, f"Duplicate id: {mod['id']}"
    assert mod["package_name"].casefold() not in packages, "Duplicate package identity"
    ids.add(mod["id"])
    packages.add(mod["package_name"].casefold())
    prefix = f"{mod['repository']}/releases/download/v{mod['version']}/"
    assert mod["download_url"].startswith(prefix), "Download must belong to the registered repository and version tag"
    assert not urlparse(mod["download_url"]).query, "Download URL cannot use mutable query parameters"
print(f"PASS: schema v1, {len(ids)} unique mod(s), repository/version download bindings")
