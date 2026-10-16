# Schedule I Mod Registry

The community-maintained index consumed by [Schedule I Mod Manager](https://github.com/schedule-one-mods/schedule-one-manager). Mod source and release ZIPs stay in their authors' repositories. This repository contains metadata only.

The client fetches [`index.json`](index.json) from:

`https://raw.githubusercontent.com/schedule-one-mods/schedule-one-mod-registry/main/index.json`

Schema version **1** lists one current release per mod. Each entry includes a stable `id`, display name, author, short summary, source repository, package name/version, exact GitHub Release ZIP URL, byte size, SHA-256 and tested compatibility. `package_name` and `version` must match the ZIP's `manifest.json`. Compatibility must match the ZIP's `compatibility.json` for game, backend, tested game versions, platforms and loader versions.

The manager downloads on demand, verifies size and SHA-256, validates package metadata and imports it into the local library. Enabling a downloaded mod uses the manager's existing compatibility and file-ownership checks. Discovery does not imply compatibility with every game build. The initial entry is Businesses 0.1.3 for Schedule I 0.4.7f5 / IL2CPP / Windows x64 / MelonLoader 0.7.3.

See [CONTRIBUTING.md](CONTRIBUTING.md) to register a mod and [the JSON Schema](schema/registry-v1.schema.json) for the precise format. Maintainers review and merge changes manually for now. There is no automatic discovery, PR merge bot, telemetry or mod binary hosting in this repository. Incompatible schema changes require a new schema version and client support.
