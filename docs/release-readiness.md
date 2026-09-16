# Release readiness — initial public preview

Reviewed September 15, 2026. This package is ready to share as an early open-source preview, not as a benchmarked guarantee of design quality.

## Verified coverage

- Eight installer tests cover both hosts, repeat installation, conflict preflight, reviewed updates and backups, local-edit preservation, destination and source symlinks, malformed management records, and empty sources.
- Dependency-free package checks cover core skill metadata, local Markdown references, showcase assets/anchors and evaluation definitions.
- GitHub CI runs those checks on Linux and macOS with Python 3.9 and 3.13.
- The showcase has been reviewed in desktop and 390-pixel layouts. Images, navigation, copy feedback and the validation disclosure were exercised.
- The imagery companion is an optional pinned submodule with its own MIT license and installer. A plain clone installs the three core skills without downloading it.

## What these checks do not establish

- Cross-model behavioral evaluation remains pending. The five evaluation scenarios are definitions, not reported trial results.
- Agent walkthroughs are not representative-user research. There is no claim of exhaustive state coverage or measured outcome improvement.
- Windows installation and cloud-account installation have not been validated.
- The core installer preflights known conflicts before writing. It is not a transaction across every destination if an unexpected filesystem failure interrupts a multi-skill install. Rerun after correcting the cause; completed managed installs are idempotent.
- Gallery imagery is an illustrative adaptation of earlier work. It is not a fidelity-critical screenshot, endorsement or proof that the new package produced those projects.

## Sharing and maintenance

Original captures and project-specific run evidence stay in ignored local folders. Public code, docs and generated showcase assets are covered by the repository's MIT license; third-party names, marks and source material are not licensed by this project. The companion retains its own license.

Before changing skill behavior, follow the learning protocol and record baseline/candidate results. Before a release, run both check commands from CONTRIBUTING.md, review the diff, and verify the published showcase if it changed. No telemetry, scheduled self-modification or automatic updates are enabled.
