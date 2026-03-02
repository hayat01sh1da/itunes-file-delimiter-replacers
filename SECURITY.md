## Supported Versions

- Only the latest code on `master` receives security updates.
- Historical versions are provided for reference and are unsupported unless the issue reproduces on the stack below.

## Ecosystem & Compatibility

| Component            | Version(s) / Tooling                | Notes |
| -------------------- | ---------------------------------- | ----- |
| OS baseline          | WSL (Ubuntu 24.4.3 LTS)            | Matches the README instructions. |
| Ruby CLI utilities   | Ruby 4.0.1 (`.ruby-version`)       | Uses standard library (`CSV`, `FileUtils`). Declare extra gems per script if needed. |
| Python CLI utilities | CPython 3.14.3 (`.python-version`) | Uses Python stdlib (`csv`, `argparse`). Introduce `requirements.txt` if third-party libs are added. |

## Backward Compatibility

- Command-line prompts and delimiter-conversion logic remain stable within Ruby 4.0.x / Python 3.14.x. Any breaking change will be announced in the README.
- Earlier interpreter majors are not tested and will not receive backports.

## Reporting a Vulnerability

Please report issues privately via **GitHub Security Advisory** (preferred) — open through the repository’s **Security → Report a vulnerability** workflow.

Acknowledgement occurs and status updates follow as soon as possible.  
After remediation we publish guidance alongside required dependency updates.
