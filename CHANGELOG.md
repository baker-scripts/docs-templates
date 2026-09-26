# Changelog

All notable changes to this project are documented here. Releases follow [Semantic Versioning](https://semver.org/).

## [1.11.0](https://github.com/baker-scripts/docs-templates/compare/v1.10.2...v1.11.0) (2026-07-11)

### Documentation

* docs: capture docs-templates version + full mkdocs dep versions in bug reports ([4c23c58](https://github.com/baker-scripts/docs-templates/commit/4c23c58))

### Maintenance

* chore: inline self-contained house Renovate config (#11) ([50f066b](https://github.com/baker-scripts/docs-templates/commit/50f066b))

### Dependencies

* 6 automated dependency updates (Renovate/Dependabot)

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.10.2...v1.11.0>

## [1.10.2](https://github.com/baker-scripts/docs-templates/compare/v1.10.1...v1.10.2) (2026-05-10)

### Fixes

* fix(plex-guide): drop attr_list anchor - conflicts with mkdocs-macros Jinja {# ([c84208c](https://github.com/baker-scripts/docs-templates/commit/c84208c))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.10.1...v1.10.2>

## [1.10.1](https://github.com/baker-scripts/docs-templates/compare/v1.10.0...v1.10.1) (2026-05-10)

### Fixes

* fix(plex-guide): explicit attr_list anchor for TV section ([bcf6f94](https://github.com/baker-scripts/docs-templates/commit/bcf6f94))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.10.0...v1.10.1>

## [1.10.0](https://github.com/baker-scripts/docs-templates/compare/v1.8.0...v1.10.0) (2026-05-10)

### Features

* feat(plex-guide): add Vizio TV; strengthen not-recommended caveat for TV apps ([de4af09](https://github.com/baker-scripts/docs-templates/commit/de4af09))
* feat(plex-guide): add Apple TV, Roku, Smart TV, mobile, and browser device sections ([087f55c](https://github.com/baker-scripts/docs-templates/commit/087f55c))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.8.0...v1.10.0>

## [1.8.0](https://github.com/baker-scripts/docs-templates/compare/v1.7.0...v1.8.0) (2026-04-27)

### Features

* feat: redesign device setup guide with Plex-specific controls ([9a54546](https://github.com/baker-scripts/docs-templates/commit/9a54546))
* feat: add remote control button references to device setup guide ([34394eb](https://github.com/baker-scripts/docs-templates/commit/34394eb))

### Fixes

* fix: replace local shfmt hook with scop/pre-commit-shfmt ([f427609](https://github.com/baker-scripts/docs-templates/commit/f427609))
* fix: corrupted lint.yml workflow (control char replacing jobs:) ([0f49003](https://github.com/baker-scripts/docs-templates/commit/0f49003))
* fix: add title frontmatter to device-setup.md template ([ac37f1f](https://github.com/baker-scripts/docs-templates/commit/ac37f1f))

### Documentation

* docs: expand 'adding to existing repo' section with device-setup.md and admin_contact guidance ([41df941](https://github.com/baker-scripts/docs-templates/commit/41df941))

### CI

* ci: add pre-commit lint workflow ([2e12f32](https://github.com/baker-scripts/docs-templates/commit/2e12f32))

### Maintenance

* chore: add CodeRabbit PR review configuration ([5f9c37d](https://github.com/baker-scripts/docs-templates/commit/5f9c37d))
* chore: shfmt --diff to --write for autofix ([6113dc2](https://github.com/baker-scripts/docs-templates/commit/6113dc2))
* chore: standardize pre-commit hooks ([0d4e21a](https://github.com/baker-scripts/docs-templates/commit/0d4e21a))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.7.0...v1.8.0>

## [1.7.0](https://github.com/baker-scripts/docs-templates/compare/v1.6.1...v1.7.0) (2026-04-05)

### Features

* feat: add device setup guide template for Fire TV Stick and Shield ([94143a3](https://github.com/baker-scripts/docs-templates/commit/94143a3))

### CI

* ci: add concurrency group, permissions, and update actions ([4bb2432](https://github.com/baker-scripts/docs-templates/commit/4bb2432))

### Maintenance

* chore: standardize Dependabot with grouping and labels ([0f054bc](https://github.com/baker-scripts/docs-templates/commit/0f054bc))

### Dependencies

* 2 automated dependency updates (Renovate/Dependabot)

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.6.1...v1.7.0>

## [1.6.1](https://github.com/baker-scripts/docs-templates/compare/v1.6.0...v1.6.1) (2026-03-21)

### Fixes

* fix: add anchor target for admonition link in plex guide template ([d86e5c7](https://github.com/baker-scripts/docs-templates/commit/d86e5c7))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.6.0...v1.6.1>

## [1.6.0](https://github.com/baker-scripts/docs-templates/compare/v1.5.0...v1.6.0) (2026-03-21)

### Features

* feat: add configurable stream monitoring to plex guide template ([0a04a26](https://github.com/baker-scripts/docs-templates/commit/0a04a26))

### CI

* ci: add timeout-minutes, pin shellcheck action version ([9c40ff6](https://github.com/baker-scripts/docs-templates/commit/9c40ff6))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.5.0...v1.6.0>

## [1.5.0](https://github.com/baker-scripts/docs-templates/compare/v1.4.1...v1.5.0) (2026-03-13)

### Fixes

* fix: escape backslash in JS regex for Python f-string compatibility ([7ff03cf](https://github.com/baker-scripts/docs-templates/commit/7ff03cf))
* fix: harden contact card against XSS and fix template defaults ([b7cbc10](https://github.com/baker-scripts/docs-templates/commit/b7cbc10))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.4.1...v1.5.0>

## [1.4.1](https://github.com/baker-scripts/docs-templates/compare/v1.4.0...v1.4.1) (2026-03-13)

### Documentation

* docs: update README and CLAUDE.md for contact card system ([5333db2](https://github.com/baker-scripts/docs-templates/commit/5333db2))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.4.0...v1.4.1>

## [1.4.0](https://github.com/baker-scripts/docs-templates/compare/v1.3.1...v1.4.0) (2026-03-13)

### Features

* feat: add telegram, discord, whatsapp, imessage contact types ([bbbdbd6](https://github.com/baker-scripts/docs-templates/commit/bbbdbd6))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.3.1...v1.4.0>

## [1.3.1](https://github.com/baker-scripts/docs-templates/compare/v1.3.0...v1.3.1) (2026-03-13)

### Maintenance

* chore: pin mkdocs to v1 to avoid breaking v2 upgrade ([82dcb2f](https://github.com/baker-scripts/docs-templates/commit/82dcb2f))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.3.0...v1.3.1>

## [1.3.0](https://github.com/baker-scripts/docs-templates/compare/v1.2.0...v1.3.0) (2026-03-13)

### Features

* feat: add contact card CSS styling and signal_username type ([b89c83f](https://github.com/baker-scripts/docs-templates/commit/b89c83f))
* feat: add contact_card macro and bot-protected contact config ([a6bde17](https://github.com/baker-scripts/docs-templates/commit/a6bde17))

### Fixes

* fix: update plex guide pricing, add Remote Watch Pass, remove /identity ([ceec626](https://github.com/baker-scripts/docs-templates/commit/ceec626))
* fix: plex guide template improvements ([b5b27ee](https://github.com/baker-scripts/docs-templates/commit/b5b27ee))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.2.0...v1.3.0>

## [1.2.0](https://github.com/baker-scripts/docs-templates/compare/v1.1.0...v1.2.0) (2026-03-12)

### Fixes

* fix: add required blank lines after jinja2 conditionals before headings ([56178cd](https://github.com/baker-scripts/docs-templates/commit/56178cd))

### Documentation

* docs: add markdownlint pragmas for plex pass table ([c92f96b](https://github.com/baker-scripts/docs-templates/commit/c92f96b))
* docs: improve plex guide template with collapsible sections and condensed device table ([8357fa1](https://github.com/baker-scripts/docs-templates/commit/8357fa1))
* docs: update plex guide template with TOC, device table, TRaSH link ([4087816](https://github.com/baker-scripts/docs-templates/commit/4087816))

### Maintenance

* chore: standardize Dependabot config ([2390a81](https://github.com/baker-scripts/docs-templates/commit/2390a81))

### Dependencies

* 1 automated dependency update (Renovate/Dependabot)

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.1.0...v1.2.0>

## [1.1.0](https://github.com/baker-scripts/docs-templates/compare/v1.0.0...v1.1.0) (2026-03-12)

### Features

* feat: add direct play and 4K streaming guide sections (#1) ([a6d2bd0](https://github.com/baker-scripts/docs-templates/commit/a6d2bd0))

### Fixes

* fix: markdownlint issues in CLAUDE.md and README ([aef2e35](https://github.com/baker-scripts/docs-templates/commit/aef2e35))

### Documentation

* docs: add CLAUDE.md with project conventions ([25d2baf](https://github.com/baker-scripts/docs-templates/commit/25d2baf))

### CI

* ci: add Dependabot for actions and pip updates ([516a316](https://github.com/baker-scripts/docs-templates/commit/516a316))

### Maintenance

* chore: add contributors section to README ([7840229](https://github.com/baker-scripts/docs-templates/commit/7840229))

### Dependencies

* 1 automated dependency update (Renovate/Dependabot)

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/compare/v1.0.0...v1.1.0>

## [1.0.0](https://github.com/baker-scripts/docs-templates/commits/v1.0.0) (2026-03-11)

### Features

* feat: add interactive setup script for plex guide ([c32b912](https://github.com/baker-scripts/docs-templates/commit/c32b912))
* feat: add plex guide template with macros variable substitution ([c374dfa](https://github.com/baker-scripts/docs-templates/commit/c374dfa))

### Fixes

* fix: serve plex guide at /plex subpath on GitHub Pages ([5c28682](https://github.com/baker-scripts/docs-templates/commit/5c28682))

### Documentation

* docs: add README with setup instructions and variable reference ([23502a7](https://github.com/baker-scripts/docs-templates/commit/23502a7))

### CI

* ci: add markdownlint, shellcheck, and yamllint workflows ([33b4304](https://github.com/baker-scripts/docs-templates/commit/33b4304))
* ci: add GitHub Actions workflow for building and deploying to Pages ([3225249](https://github.com/baker-scripts/docs-templates/commit/3225249))

### Maintenance

* chore: add GitHub issue and PR templates ([36f829d](https://github.com/baker-scripts/docs-templates/commit/36f829d))
* chore: add placeholder dirs for future plan and runbook templates ([2add98b](https://github.com/baker-scripts/docs-templates/commit/2add98b))
* chore: initial repo setup with MIT license and gitignore ([21e0ead](https://github.com/baker-scripts/docs-templates/commit/21e0ead))

**Full Changelog**: <https://github.com/baker-scripts/docs-templates/commits/v1.0.0>
