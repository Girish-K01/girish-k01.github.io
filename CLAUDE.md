# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal academic site for Girish Kulathumani (https://girish-k01.github.io), built on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template (itself a fork of Minimal Mistakes). There is no test suite or linter; "verifying" a change means building the site and checking the rendered page.

## Commands

```bash
bundle install                        # install Ruby gems (Gemfile.lock is gitignored)
bundle exec jekyll serve -l -H localhost   # local dev server with livereload at http://localhost:4000
bundle exec jekyll build              # one-off build into _site/
```

- `_config.yml` changes are **not** picked up by `jekyll serve`; restart the server.
- HTML is minified by `_layouts/compress.html` except when `JEKYLL_ENV=development`, so inspect output with that env set if whitespace matters.

JavaScript bundle (only needed when editing `assets/js/_main.js` or `assets/js/plugins/*`):

```bash
pnpm install          # or npm install
npm run build:js      # uglifies jQuery + plugins + _main.js into assets/js/main.min.js
```

`assets/js/main.min.js` is committed and is what the site loads; `_main.js` and `plugins/` are excluded from the Jekyll build. Always rebuild and commit `main.min.js` after editing JS sources.

## Deployment

Pushing to `master` triggers `.github/workflows/jekyll.yml`, which builds with Ruby 3.1 (`JEKYLL_ENV=production`) and deploys to GitHub Pages. There is no other deploy step.

## Architecture

**Content sources → pages**

| Section (nav from `_data/navigation.yml`) | Page template | Content source |
|---|---|---|
| About (`/`) | `_pages/about.md` (+ `assets/css/about-style.css`) | inline |
| Publications (`/publications/`) | `_pages/publications.html` | `_publications/*.md` collection |
| Blog (`/blog/`) | `_pages/year-archive.html` (+ `assets/css/year-archive-style.css`) | `_posts/*.md` |
| Resume (`/cv/`) | `_pages/cv-json.md` → `_includes/cv-template.html` | `_data/cv.json` (JSON Resume format, read as `site.data.cv`); PDF at `files/cv.pdf` |

Also in `_pages/`: `tag-archive.html` (`/tags/`, linked from post tags), `sitemap.md` (linked from the footer), and `404.md`. Comments and category archives have been removed from the template.

**Publications**: grouped by the `category` front-matter key, which must match a key under `publication_category` in `_config.yml` (`manuscripts`, `conferences`); a publication with any other category won't appear on the categorized page. The listing template reads `title`, `authors`, `venue`, `date`, `paperurl`, `codeurl`, `teaser`, `excerpt`. Individual publication pages use `_layouts/single.html` via `defaults` in `_config.yml`.

**Blog posts**: each post sets an explicit `permalink` and an `image` (under `/images/`); posts belong to the "GreyLattice" series mirrored from greylattice.substack.com. `future: true` is set, so future-dated posts still publish. `image` is only used for the card on `/blog/` (rendered ~180px tall, ≤450px wide), so add it as WebP at ~900px wide rather than a full-size PNG. MathJax is loaded only on pages with `math: true` in front matter.

**Styling**: `assets/css/main.scss` is the single Sass entry point, importing from `_sass/`. Theme colors are CSS custom properties: `_sass/theme/_default.scss` defines them on `:root`, `_sass/theme/_dark.scss` overrides them under `html[data-theme="dark"]`. Page-specific stylesheets in `assets/css/` (cv, about, year-archive) are plain CSS loaded via `<link>` from the page itself and must define their own `[data-theme="dark"]` variants. Custom publication styles live in `_sass/_custom_publications.scss`. `_sass/vendor/` is third-party — don't edit.

**Dark mode**: an inline script in `_includes/head.html` sets the initial theme before CSS loads (avoids a light flash); it must not contain `//` comments because `_layouts/compress.html` collapses newlines. `assets/js/_main.js` toggles `data-theme="dark"` on `<html>` (button `#theme-toggle` in `_includes/masthead.html`), persisting the choice in `localStorage` and otherwise following `prefers-color-scheme`. Any new styling must work in both themes, ideally by using the `--global-*` variables rather than hard-coded colors.

**Site-wide settings**: author sidebar/profile links, social links, analytics (GA4), SEO, and plugin list all live in `_config.yml`. Sidebar markup is `_includes/author-profile.html`; `<head>` additions go in `_includes/head/custom.html`.
