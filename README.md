# docs-templates

[![Build Plex Guide](https://github.com/baker-scripts/docs-templates/actions/workflows/build.yml/badge.svg)](https://github.com/baker-scripts/docs-templates/actions/workflows/build.yml)
[![Lint](https://github.com/baker-scripts/docs-templates/actions/workflows/lint.yml/badge.svg)](https://github.com/baker-scripts/docs-templates/actions/workflows/lint.yml)
[![Live Preview](https://img.shields.io/badge/Live_Preview-GitHub_Pages-blue)](https://baker-scripts.github.io/docs-templates/plex/)

MkDocs documentation templates with variable substitution. Fork, customize, and deploy your own documentation site.

## Available Templates

| Template | Description | Live Preview |
|----------|-------------|--------------|
| [Plex Guide](plex-guide/) | User-facing guide for Plex media servers | [Preview](https://baker-scripts.github.io/docs-templates/plex/) |

**Coming soon:** Plan templates, runbook templates.

## Quick Start (Plex Guide)

### Option 1: Interactive Setup (Recommended)

```bash
git clone https://github.com/baker-scripts/docs-templates.git
cd docs-templates/plex-guide
./setup.sh
```

The script will:

1. Ask for your server details (name, URLs, features)
2. Generate a configured `mkdocs.yml` from the sample
3. Build static HTML or start a live preview

### Option 2: Manual Setup

```bash
git clone https://github.com/baker-scripts/docs-templates.git
cd docs-templates/plex-guide

# Copy sample config and edit it
cp mkdocs.sample.yml mkdocs.yml
# Edit the `extra:` section in mkdocs.yml with your values

# Install dependencies and build
pip install -r requirements.txt
mkdocs build        # Static HTML in site/
# or
mkdocs serve        # Live preview at http://localhost:8000
```

### Option 3: Docker

```bash
cd docs-templates/plex-guide
cp mkdocs.sample.yml mkdocs.yml
# Edit mkdocs.yml with your values

docker run --rm -v "$(pwd):/docs" squidfunk/mkdocs-material build
```

## Adding to an Existing MkDocs Repo

If you already have a MkDocs site and want to add the Plex guide:

1. **Install the macros plugin:**

   ```bash
   pip install mkdocs-macros-plugin
   ```

2. **Add the plugin to your `mkdocs.yml`:**

   ```yaml
   plugins:
     - macros:
         render_by_default: false
   ```

   > `render_by_default: false` prevents the plugin from processing `{{ }}` in your other pages (like Docker commands). Only pages with `render_macros: true` in their frontmatter will use variable substitution.

3. **Add variables to `extra:` in your `mkdocs.yml`:**

   ```yaml
   extra:
     server_name: "My Server"
     admin_name: "Admin"
     admin_contact: "Message Admin"
     media_url: "app.plex.tv"
     has_request_system: false
     # ... see Variable Reference below
   ```

4. **Copy `plex-guide/docs/index.md`** into your docs directory.

5. **Add `render_macros: true`** to the page's frontmatter (already included in the template).

## Variable Reference

### Required

| Variable | Description | Example |
|----------|-------------|---------|
| `server_name` | Display name for your server | `"My Plex Server"` |
| `admin_name` | Server admin's first name | `"John"` |
| `admin_contact` | How users should reach you | `"Text John"` |
| `media_url` | Plex access URL (no `https://`) | `"plex.example.com"` |

### Optional Features

Set to `true` to show the section, `false` to hide it.

| Variable | Default | Description |
|----------|---------|-------------|
| `has_request_system` | `true` | Overseerr/Jellyseerr request system |
| `request_url` | `""` | Request system URL |
| `has_discord` | `false` | Discord notification server |
| `discord_url` | `""` | Discord invite link |
| `has_newsletter` | `false` | Tautulli newsletter |
| `newsletter_url` | `""` | Newsletter URL |
| `has_guide_url` | `false` | Public guide link at top of page |
| `guide_url` | `""` | Public URL for the guide |
| `has_plex_pass` | `true` | Plex Pass features section |
| `has_plex_home` | `false` | Plex Home notes |
| `has_direct_play` | `true` | Direct play optimization guide |
| `has_4k_content` | `true` | 4K streaming section |
| `has_migration` | `false` | Watch history migration section |
| `show_costs` | `false` | Server cost information |
| `server_cost` | `""` | Monthly cost string |

## How It Works

Templates use [mkdocs-macros-plugin](https://mkdocs-macros-plugin.readthedocs.io/) for Jinja2 variable substitution. Variables defined in the `extra:` section of `mkdocs.yml` are available as `{{ variable_name }}` in markdown files.

Conditional sections use `{% if feature_flag %}...{% endif %}` to show/hide content based on your configuration.

## Theme Features

The template uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) with a dark-first theme (slate) and light mode toggle. The following features are enabled:

| Feature | Description |
|---------|-------------|
| `navigation.sections` | Groups top-level sections in the sidebar with visible headers |
| `navigation.instant` | Loads pages via XHR without full page reload for faster navigation |
| `toc.follow` | Automatically scrolls the table of contents sidebar to highlight the active heading |
| `search.suggest` | Shows search term suggestions as you type in the search bar |
| `search.highlight` | Highlights matching search terms on the page after navigating from search results |
| `content.code.copy` | Adds a copy-to-clipboard button on all code blocks |
| `content.code.annotate` | Enables numbered annotations inside code blocks with expandable tooltips |
| `content.tabs.link` | Syncs tab selection across all tabbed content blocks on the page |

## Deployment

### GitHub Pages (automatic)

This repo includes a GitHub Action that builds the template with sample values and deploys to GitHub Pages. Fork the repo, enable Pages in your fork's settings, and your guide will be available at `https://<your-username>.github.io/docs-templates/plex/`.

### Static Hosting

Run `mkdocs build` and upload the `site/` directory to any web server (Nginx, Apache, Caddy, S3, Netlify, Vercel, etc.).

### MkDocs Serve

Run `mkdocs serve` for a local development server with live reload at `http://localhost:8000`.

## Disclaimer

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This project is not affiliated with or endorsed by Plex, Inc. Plex is a registered trademark of Plex, Inc.

## License

[MIT](LICENSE)
