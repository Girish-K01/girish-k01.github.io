# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal academic site for Girish Kulathumani (https://girish-k01.github.io), built on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template (itself a fork of Minimal Mistakes). There is no test suite or linter; "verifying" a change means building the site and checking the rendered page.

## Commands

```bash
bundle install                        # install Ruby gems from the committed Gemfile.lock (Jekyll 4.4, Ruby 4.0)
bundle exec jekyll serve -l -H localhost   # local dev server with livereload at http://localhost:4000
bundle exec jekyll build              # one-off build into _site/
```

- `_config.yml` changes are **not** picked up by `jekyll serve`; restart the server.
- HTML is minified by `_layouts/compress.html` except when `JEKYLL_ENV=development`, so inspect output with that env set if whitespace matters.
- Templates build URLs from `{{ base_path }}` (`_includes/base_path`): absolute `site.url` in production (canonical and og tags need it), root-relative under `jekyll serve`, so the dev site works at both `localhost` and `127.0.0.1`. Don't hard-code `site.url` into asset links: from a `127.0.0.1` page, absolute `localhost` font URLs are cross-origin, the browser blocks them, and icons render as boxes.
- WEBrick (the dev server) logs `ERROR Errno::ECONNRESET … io_fillbuf` when the browser drops an idle connection. It's harmless and doesn't happen on GitHub Pages.

JavaScript bundle (only needed when editing `assets/js/_main.js` or `assets/js/plugins/*`):

```bash
pnpm install          # or npm install
npm run build:js      # uglifies jQuery + plugins + _main.js into assets/js/main.min.js
```

`assets/js/main.min.js` is committed and is what the site loads; `_main.js` and `plugins/` are excluded from the Jekyll build. Always rebuild and commit `main.min.js` after editing JS sources.

## Deployment

Pushing to `master` triggers `.github/workflows/jekyll.yml`, which builds with Ruby 4.0 from the committed `Gemfile.lock` (`JEKYLL_ENV=production`) and deploys to GitHub Pages. The repo's Pages source must be **GitHub Actions** (Settings → Pages → Build and deployment). If it is "Deploy from a branch", GitHub's built-in builder also builds `master` with the old `github-pages` gem (Jekyll 3.10, ignoring the Gemfile) and races this workflow; whichever finishes last goes live. Check with `gh api repos/Girish-K01/girish-k01.github.io/pages --jq .build_type` (want `workflow`). To test a build without publishing, push a branch and run `gh workflow run jekyll.yml --ref <branch>`; the deploy job only runs on `master`, and the `github-pages` environment only accepts `master` anyway. The site does **not** use the `github-pages` gem, so GitHub's implicit plugins (optional front matter, relative links, titles from headings, `site.github`) are not available; add any plugin you need to both `Gemfile` and `plugins:` in `_config.yml`. If you change the Ruby version, update the workflow's `ruby-version` too, and after changing gems run `bundle lock` so the lockfile keeps its Linux platforms for CI.

## Architecture

**Content sources → pages**

| Section (nav from `_data/navigation.yml`) | Page template | Content source |
|---|---|---|
| About (`/`) | `_pages/about.md` (+ `assets/css/about-style.css`) | inline |
| Publications (`/publications/`) | `_pages/publications.html` | `_publications/*.md` collection |
| Blog (`/blog/`) | `_pages/year-archive.html` (+ `assets/css/year-archive-style.css`) | `_posts/*.md` |
| Resume (`/cv/`) | `_pages/cv-json.md` → `_includes/cv-template.html` | `_data/cv.json` (JSON Resume format, read as `site.data.cv`); PDF at `files/cv.pdf` |

Also in `_pages/`: `tag-archive.html` (`/tags/`, linked from post tags), `sitemap.md` (linked from the footer), and `404.md`. Comments and category archives have been removed from the template.

**Publications**: grouped by the `category` front-matter key, which must match a key under `publication_category` in `_config.yml` (`manuscripts`, `conferences`); a publication with any other category won't appear on the categorized page. The listing template reads `title`, `authors`, `venue`, `date`, `paperurl`, `codeurl`, `teaser`, `excerpt`. Individual publication pages use `_layouts/single.html` via `defaults` in `_config.yml`. The page's `classes: page--publications` front matter is output on `<body>` by `_layouts/default.html`, and `_sass/_custom_publications.scss` is scoped to that class (any page can use `classes:` the same way).

**CV**: dates in `_data/cv.json` are `YYYY-MM`, `YYYY` or `Present`. Render them with `{% include cv-date.html date=... %}`, never the raw `date` filter: Liquid can't parse `YYYY-MM` (it prints it unformatted) and reads a bare `YYYY` as a Unix timestamp (it prints 1970). Entries render in file order, so keep each list newest first. Publications take an optional `authors` string (HTML allowed; the owner's name is wrapped in `<b>`). The page's "Download Resume (PDF)" button serves `files/cv.pdf`: the owner's resume is the source of truth, so when it changes, replace that PDF and update `cv.json`, `_publications/` and `_pages/about.md` to match.

**Blog posts**: each post sets an explicit `permalink` and an `image` (under `/images/`); posts belong to the "GreyLattice" series mirrored from greylattice.substack.com. `future: true` is set, so future-dated posts still publish. `image` is only used for the card on `/blog/` (rendered ~180px tall, ≤450px wide), so add it as WebP at ~900px wide rather than a full-size PNG. MathJax is loaded only on pages with `math: true` in front matter.

**Styling**: `assets/css/main.scss` is the single Sass entry point, importing from `_sass/`. Theme colors are CSS custom properties: `_sass/theme/_default.scss` defines them on `:root`, `_sass/theme/_dark.scss` overrides them under `html[data-theme="dark"]`. Page-specific stylesheets in `assets/css/` (cv, about, year-archive) are plain CSS loaded via `<link>` from the page itself and must define their own `[data-theme="dark"]` variants. Custom publication styles live in `_sass/_custom_publications.scss`. `_sass/vendor/` is third-party — don't edit. Sass is compiled by Dart Sass (`sass-embedded`); the template SCSS uses deprecated syntax (`@import`, `/` division, global functions), so those warnings are silenced under `sass.silence_deprecations` in `_config.yml`. They will become errors in Dart Sass 3.0, so don't upgrade `sass-embedded` past 1.x without migrating the SCSS. Sass does not evaluate functions inside a CSS custom property: write `--x: #{mix(...)}`, not `--x: mix(...)` (which is emitted verbatim as an invalid colour). `#{` is interpolated even inside `/* */` comments, so don't write it there.

**Inline scripts**: `_layouts/compress.html` joins every line of the page in production, so an inline `<script>` must never use `//` comments; everything after the first one gets commented out and the script dies with a syntax error (this silently broke the publication filters). Use `/* */` or `{% comment %}`. `jekyll serve` skips compression, so this only shows up in a production build.

**Dark mode**: an inline script in `_includes/head.html` sets the initial theme before CSS loads (avoids a light flash). `assets/js/_main.js` toggles `data-theme="dark"` on `<html>` from `#theme-toggle` in `_includes/masthead.html`, persisting the choice in `localStorage` (always wrapped in try/catch) and otherwise following `prefers-color-scheme`. The toggle is an `<a href="#" role="button">`, not a `<button>`: the nav CSS and `jquery.greedy-navigation.js` treat every `<button>` inside `#site-nav` as the hamburger menu, so don't add other buttons there. Any new styling must work in both themes and meet WCAG AA contrast (4.5:1), ideally by using the `--global-*` variables rather than hard-coded colors.

**Site-wide settings**: author sidebar/profile links, social links, analytics (currently disabled; the comment above `analytics:` says how to re-enable GA4), SEO, and plugin list all live in `_config.yml`. Sidebar markup is `_includes/author-profile.html`; `<head>` additions go in `_includes/head/custom.html`.
