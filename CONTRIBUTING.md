# Register a mod

1. Publish your mod source and a versioned ZIP in a public GitHub repository release tagged `v<version>` (for example `v0.1.3`). The archive must contain `manifest.json`, `compatibility.json`, and exactly one `Mods/*.dll`. README, changelog, icon and third-party notices are optional supported extras. Use the current Businesses package as a format example. Do not include game files, saves, SDKs or the loader itself.
2. Fork this registry and add an entry to `index.json`, following the existing entry. Pick a stable lowercase hyphenated `id`; IDs and package names must be unique. Use three numeric version components. Do not change an existing mod's identity during updates.
3. Record the exact uploaded ZIP URL, its size in bytes and its SHA-256 hash. Downloads must belong to your registered repository and matching version tag. Do not use `/latest/` URLs or mutable branch archives. Never replace a published asset in place; publish a new version and submit an index update.
4. Supply the package's tested game/backend/platform/loader compatibility. Claim only versions you have tested. The index does not make a binary safe or guarantee it cannot crash.
5. Validate locally with `python -m pip install -r requirements.txt` then `python validate.py`. Open a PR explaining the mod or update and your compatibility testing. Maintainers review the source, license/notices, package metadata, URL, checksum and test evidence before merging.

GitHub-hosted ZIPs and Windows x64 single-DLL packages are the initial supported format. Dependency metadata currently supports MelonLoader only. Community review/CI automation, multiple release histories and additional hosting platforms can be designed separately.
