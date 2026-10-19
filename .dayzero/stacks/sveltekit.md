# Stack guide: SvelteKit (sveltekit)

Checked: 2026-10-19. Covers SvelteKit 2 with Svelte 4 or 5.

## 1. Detection signals

- Strong: `svelte.config.js` importing `@sveltejs/kit` or an adapter; `src/routes/+page.svelte`.
- Weak: `package.json` dependency `svelte`.
- Used as the UI guide in hybrids (Tauri, Laravel with Inertia and Svelte).

## 2. Entry point

- `src/routes/+layout.svelte` wraps everything; `src/routes/+page.svelte` is `/`.
- `src/hooks.server.ts` `handle` runs before every request and can redirect.

## 3. Screens or commands

- Globs: `src/routes/**/+page.svelte`. `+layout.svelte`, `+error.svelte` are not screens.
- Route groups `(group)` and params `[slug]` are URL rules, not separate screens.

## 4. Navigation

- `<a href>`, `goto(`, `redirect(` in `+page.server.ts` / `+layout.server.ts` load functions, `hooks.server.ts` redirects.
- Form action results that `redirect(303, ...)` count as navigation.

## 5. Forms and inputs

- `<form method="POST">` with form actions in `+page.server.ts`; inputs with `required`; server validation returning `fail(400, ...)` counts as required.
- sveltekit-superforms with Zod/Valibot schemas.

## 6. Auth

- Lucia, Auth.js for SvelteKit (`@auth/sveltekit`, providers = OAuth), Supabase, Firebase, custom session cookies in `hooks.server.ts`.

## 7. Billing

- Stripe in form actions or `src/routes/api/**/+server.ts`; webhook route that sets a plan = `paid_active`.

## 8. Permissions

- Browser APIs: `Notification.requestPermission(`, `navigator.geolocation`, `getUserMedia(`.

## 9. User-facing text

- Markup in `.svelte` files, `$lib/i18n`, paraglide `messages/*.json`, `svelte-i18n`, `<svelte:head><title>`.

## 10. Styles, api, jobs

### styles

- `src/app.css`, `<style>` blocks in components, Tailwind (`text-xs` 12px, `text-sm` 14px, `text-base` 16px).
- Low contrast: helper text colors against the page background (WCAG AA 4.5:1).

### api

- `src/routes/**/+server.ts` endpoints. Public API = user-facing token auth.

### jobs

- Cron via platform config, webhook routes, email senders in `$lib/server`.

## 11. First-value hints

- `first_value`: the first page where the user publishes, saves or sees their own item.
- `upgrade`: pricing page → checkout action → webhook sets plan → unlocked page.
- `invite`: invite action → email link with a token → invitee joins shared content.
- `return`: login → `hooks.server.ts` session → dashboard with existing data.

## 12. Known traps

- Exclude: `.svelte-kit/`, `build/`, `node_modules/`, `src/**/*.test.ts`, `*.d.ts`.
- `+page.ts` / `+page.server.ts` are data and actions for the screen in the same folder, not separate screens.
- `$lib/server` code never runs in the browser; it can still gate navigation.
