# docs-templates

MkDocs documentation templates with `mkdocs-macros-plugin` for Jinja2 variable substitution.

## Structure

- `plex-guide/` — Plex server user guide template
  - `docs/index.md` — templatized guide with `{{ variable }}` references
  - `main.py` — mkdocs-macros hook: `contact_card()` macro + frontmatter resolution
  - `mkdocs.sample.yml` — sample config (users copy to `mkdocs.yml`, which is gitignored)
  - `setup.sh` — interactive setup script
  - `requirements.txt` — minimal pip dependencies (mkdocs pinned to v1)
- `plans/`, `runbooks/` — future template directories

## Key Patterns

- **`mkdocs.sample.yml`** — users copy to `mkdocs.yml` to prevent PII leaks. `mkdocs.yml` is gitignored.
- **Variables** — defined in `extra:` section of `mkdocs.yml`, referenced as `{{ variable_name }}` in markdown
- **Conditional sections** — `{% if has_feature %}...{% endif %}` for optional content
- **markdownlint** — Jinja2 inside tables requires disabling MD055/MD056/MD060; `{% if %}` before `---` requires disabling MD003

## Development

- Build: use a venv or Docker, never system-wide pip

  ```bash
  cd plex-guide
  python3 -m venv .venv
  .venv/bin/pip install -r requirements.txt
  cp mkdocs.sample.yml mkdocs.yml
  .venv/bin/mkdocs build
  ```

- Lint: `npx markdownlint-cli2 "**/*.md"` and `shellcheck plex-guide/setup.sh`
- CI runs markdownlint, shellcheck, yamllint on all PRs
- GitHub Pages deploys from GHA workflow (plex guide at `/plex/` subpath)

## Contact Card System

`main.py` provides a `contact_card()` macro with bot-protected contact info:

- Values are base64-encoded at build time, decoded by JS at runtime
- Inline CSS styles the card (border, rounded corners, dividers, preferred badge)
- Supported types: `email`, `phone`, `signal_url`, `signal_username`, `telegram`, `discord`, `whatsapp`, `imessage`
- `signal_username` and `discord` render as plain text (no clickable link)
- `telegram` → `t.me/`, `whatsapp` → `wa.me/`, `imessage` → `sms:`, `phone` → `tel:`
- `noscript` fallback shows values without JS decoding

## Rules

- This is a **public repo** — no local paths, infrastructure refs, or personal config
- All scripts must pass `shellcheck` with no warnings
- All markdown must pass `markdownlint-cli2` with the repo's `.markdownlint.yaml`
- New variables must be added to: `mkdocs.sample.yml`, `setup.sh`, `README.md` variable reference
- New contact types must be added to: `main.py` (JS decoder + `_build_href` + `_display_value`), `mkdocs.sample.yml`
- Conditional sections must toggle cleanly (no empty sections or broken refs when disabled)
- MkDocs pinned to v1 (`>=1.6,<2`) — v2 removes plugin system with no migration path
