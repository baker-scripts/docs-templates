# docs-templates

[![Build Plex Guide](https://github.com/baker-scripts/docs-templates/actions/workflows/build.yml/badge.svg)](https://github.com/baker-scripts/docs-templates/actions/workflows/build.yml)
[![Lint](https://github.com/baker-scripts/docs-templates/actions/workflows/lint.yml/badge.svg)](https://github.com/baker-scripts/docs-templates/actions/workflows/lint.yml)
[![Release](https://img.shields.io/github/v/release/baker-scripts/docs-templates)](https://github.com/baker-scripts/docs-templates/releases)
[![Live Preview](https://img.shields.io/badge/Live_Preview-GitHub_Pages-blue)](https://baker-scripts.github.io/docs-templates/plex/)

MkDocs documentation templates with Jinja2 variable substitution (`mkdocs-macros-plugin`). Fork, set your values, and deploy your own site.

| Template | Description | Live preview |
| --- | --- | --- |
| [Plex Guide](plex-guide/) | User-facing guide for a Plex media server | [Preview](https://baker-scripts.github.io/docs-templates/plex/) |

`plans/` and `runbooks/` are empty placeholders for future templates.

## Quick Start (Plex Guide)

Interactive:

```bash
git clone https://github.com/baker-scripts/docs-templates.git
cd docs-templates/plex-guide
./setup.sh
```

`setup.sh` prompts for server details and feature toggles, writes `mkdocs.yml` from `mkdocs.sample.yml`, then offers to build static HTML, start a live preview, or skip the build. It needs `mkdocs` on your `PATH` to build.

Manual:

```bash
cd docs-templates/plex-guide
cp mkdocs.sample.yml mkdocs.yml   # edit the extra: section
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs build            # static HTML in site/
.venv/bin/mkdocs serve            # live preview at http://localhost:8000
```

Docker:

```bash
cd docs-templates/plex-guide
cp mkdocs.sample.yml mkdocs.yml
docker run --rm -v "$(pwd):/docs" squidfunk/mkdocs-material build
```

`mkdocs.yml` is gitignored so personal values stay out of commits. MkDocs is pinned to v1 (`>=1.6.1,<2`).

## Configuration

Set variables in the `extra:` section of `mkdocs.yml`. Reference them as `{{ variable_name }}` in markdown. Conditional sections use `{% if has_feature %}...{% endif %}`.

Required:

| Variable | Description | Example |
| --- | --- | --- |
| `server_name` | Display name for your server | `"My Plex Server"` |
| `admin_name` | Admin's first name | `"John"` |
| `admin_contact` | How users reach you | `"Text John"` |
| `media_url` | Plex access URL, no `https://` | `"plex.example.com"` |

Optional features (`true` shows the section, `false` hides it). Defaults are from `mkdocs.sample.yml`:

| Variable | Default | Description |
| --- | --- | --- |
| `has_request_system` | `true` | Seerr request system |
| `request_url` | `"requests.example.com"` | Request system URL |
| `has_wizarr_join` | `false` | Wizarr self-service invites |
| `wizarr_join_url` | `""` | Wizarr public invite URL |
| `invite_url_example` | `""` | Sample invite link in the sign-up steps; empty hides it |
| `has_discord` | `false` | Discord server |
| `discord_url` | `""` | Discord invite link |
| `has_newsletter` | `false` | Tautulli newsletter |
| `newsletter_url` | `""` | Newsletter URL |
| `has_guide_url` | `false` | Public guide link at the top of the page |
| `guide_url` | `""` | Public URL for the guide |
| `has_plex_pass` | `true` | Plex Pass features section |
| `has_plex_home` | `false` | Plex Home notes |
| `has_direct_play` | `true` | Direct play optimization guide |
| `has_4k_content` | `true` | 4K streaming section |
| `has_migration` | `false` | Watch history migration section |
| `show_costs` | `false` | Server cost information |
| `server_cost` | `""` | Monthly cost string |
| `speedtest_url` | `""` | Speed test URL; falls back to `fast.com` |
| `has_stream_monitoring` | `false` | Master toggle for the "Your Stream Was Stopped" section |
| `has_geo_restriction` | `false` | Geo-based stream kills (VPN, out-of-country) |
| `has_transcode_protection` | `false` | 4K transcode protection kills |
| `has_stream_limits` | `false` | Per-user simultaneous stream limit kills |
| `has_impossible_travel` | `false` | Impossible-travel detection kills |
| `has_fire_tv` | `true` | Fire TV Stick setup instructions |
| `has_shield` | `true` | NVIDIA Shield setup instructions |

`setup.sh` does not prompt for `has_wizarr_join`, `wizarr_join_url`, `invite_url_example`, `has_fire_tv`, `has_shield`, or `contact_methods`. Set those in `mkdocs.yml` by hand.

### Contact card

`contact_methods` configures a contact card at the bottom of the guide. Values are base64-encoded at build time and decoded by JavaScript at runtime; a `noscript` fallback shows them undecoded.

```yaml
contact_methods:
  - type: signal_url
    label: "Message on Signal"
    value: "https://signal.me/#eu/..."
    preferred: true    # shows a "preferred" badge
  - type: email
    label: "Email"
    value: "admin@example.com"
```

| Type | Behavior | Value format |
| --- | --- | --- |
| `email` | `mailto:` link | `admin@example.com` |
| `phone` | `tel:` link | `+15551234567` |
| `signal_url` | Clickable Signal invite | `https://signal.me/#eu/...` |
| `signal_username` | Plain text | `username.123` |
| `telegram` | `t.me/` link | `username` |
| `discord` | Plain text | `username` |
| `whatsapp` | `wa.me/` link | `+15551234567` |
| `imessage` | `sms:` link | `+15551234567` |

## Usage

### Add the guide to an existing MkDocs site

1. Install the plugin: `pip install mkdocs-macros-plugin`.
2. Enable it in your `mkdocs.yml`:

   ```yaml
   plugins:
     - macros:
         render_by_default: false
   ```

   `render_by_default: false` stops the plugin from processing `{{ }}` in your other pages (such as Docker commands). Only pages with `render_macros: true` in their frontmatter get substitution; the template pages already set it.

3. Add the variables above to `extra:`.
4. Copy the template pages into your docs directory:

   ```bash
   cp plex-guide/docs/index.md your-docs/guides/plex/index.md
   cp plex-guide/docs/device-setup.md your-docs/guides/plex/device-setup.md
   ```

   If the template is a git submodule, run these copies in your build pipeline and do not edit the local copies.
5. Copy `plex-guide/main.py` next to your `mkdocs.yml`. It provides the `contact_card()` macro that `index.md` calls.
6. If you use both pages, make `admin_contact` a cross-page link. The contact anchor is generated from the `## Contact {{ admin_name }}` heading, so it exists only on `index.md` (for `admin_name: "AJ"` it is `#contact-aj`):

   ```yaml
   admin_contact: "[Contact Admin](index.md#contact-aj)"
   ```

   A same-page anchor fails the build in strict mode when the macro expands on `device-setup.md`.
7. Gitignore the copies so they always come from the template:

   ```gitignore
   docs/guides/plex/index.md
   docs/guides/plex/device-setup.md
   ```

### Theme

The sample config uses Material for MkDocs with a dark-first palette (slate) and a light toggle. Enabled features: `navigation.sections`, `navigation.instant`, `toc.follow`, `search.suggest`, `search.highlight`, `content.code.copy`, `content.code.annotate`, and `content.tabs.link`.

### Deployment

- GitHub Pages: the `Build Plex Guide` workflow builds with the sample config and deploys to Pages on pushes to `main` that touch `plex-guide/**`. In a fork, enable Pages; the guide serves at `https://<your-username>.github.io/docs-templates/plex/`.
- Static hosting: run `mkdocs build` and upload `site/` to any web server.

## Development

```bash
npx markdownlint-cli2 "**/*.md"
shellcheck plex-guide/setup.sh
yamllint -d relaxed .
```

CI runs markdownlint, ShellCheck, and yamllint on pull requests. Adding a variable means updating `mkdocs.sample.yml`, `setup.sh`, and the table above. Adding a contact type means updating `main.py` and `mkdocs.sample.yml`.

## Contributing

Issues and pull requests welcome. See the [contributing guidelines](https://github.com/baker-scripts/.github/blob/main/CONTRIBUTING.md); [open an issue](https://github.com/baker-scripts/docs-templates/issues) to discuss larger changes.

## Disclaimer

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This project is not affiliated with or endorsed by Plex, Inc. Plex is a registered trademark of Plex, Inc.

## License

[MIT](LICENSE)
