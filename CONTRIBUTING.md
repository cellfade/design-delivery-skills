# Contributing

Keep changes small and grounded in an observed problem. Include an anonymized reproduction, expected outcome, candidate change and actual checks. Do not commit client artifacts, credentials, private research or raw conversations.

Run `python3 scripts/check_package.py` and `python3 -m unittest discover -s tests -v`. The package check validates the supported frontmatter format and local references. Structural checks are not behavioral evaluations; report them separately.

New rules should help a class of tasks without overriding user choices. Prefer optional references to longer entrypoints. Use the learning protocol for behavior changes. Maintainer review precedes merge and installation updates.
