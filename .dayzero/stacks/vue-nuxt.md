# Stack guide: Vue and Nuxt (vue-nuxt)

Checked: 2026-10-19. Covers Nuxt 3 and plain Vue 3 SPAs (Vite, vue-router).

## 1. Detection signals

- Strong: `nuxt.config.(ts|js)`; or `src/main.(ts|js)` calling `createApp(` with a `.vue` root component.
- Weak: `package.json` dependency `nuxt` or `vue`.
- Used as the UI guide in `server_js_ui` hybrids (Laravel or Rails with Inertia and Vue).

## 2. Entry point

- Nuxt: `app.vue` → `<NuxtPage />`; `pages/index.vue` is `/`. Global middleware in `middleware/*.global.ts` runs first.
- Vue SPA: `createApp(App).use(router)` → the route for `/` in the router file.

## 3. Screens or commands

- Globs: `pages/**/*.vue` (Nuxt file routes), `src/views/**`, `src/pages/**`, components used as route `component:`.
- `layouts/*.vue` wrap pages and are not screens.

## 4. Navigation

- `<NuxtLink to>`, `<RouterLink>`, `navigateTo(`, `router.push(`, `definePageMeta({ middleware })`.
- Route middleware in `middleware/*.ts` (`defineNuxtRouteMiddleware`) and `router.beforeEach` guards.

## 5. Forms and inputs

- `v-model` inputs with `required`, VeeValidate rules, Zod/Valibot schemas, FormKit.
- Count server-side rejections too: `server/api/**` handlers that throw `createError` on a missing field.

## 6. Auth

- `@sidebase/nuxt-auth` (providers: GitHub, Google = OAuth), `nuxt-auth-utils`, Supabase, Firebase, Lucia.
- Verification: a page waiting for an email link plus middleware checking a verified flag.

## 7. Billing

- Stripe (`stripe.checkout.sessions.create` in `server/api/**`), Lemon Squeezy, Paddle.
- Paid flag: webhook handler that sets a plan; a success URL alone is not `paid_active`.

## 8. Permissions

- Browser APIs: `Notification.requestPermission(`, `navigator.geolocation`, `getUserMedia(`.

## 9. User-facing text

- Template text in `.vue` files, `locales/*.json`, `@nuxtjs/i18n`, `vue-i18n` messages, `useHead` / `useSeoMeta` titles.

## 10. Styles, api, jobs

### styles

- `assets/**/*.css`, `<style scoped>` blocks, Tailwind (`text-xs` 12px, `text-sm` 14px, `text-base` 16px), UnoCSS, Vuetify themes.

### api

- Nitro routes in `server/api/**` and `server/routes/**`. Public API = user-facing token auth, not only session cookies.

### jobs

- Nitro tasks / scheduled tasks, `server/plugins` with cron, queue workers, email senders.

## 11. First-value hints

- `first_value`: the first page where the user creates or sees their own item.
- `upgrade`: pricing page or limit error → `server/api` checkout → webhook sets plan → unlocked page.
- `invite`: invite form → email link with a token → invitee joins the shared workspace.
- `return`: login or magic link → middleware → dashboard with existing data.

## 12. Known traps

- Exclude: `.nuxt/`, `.output/`, `node_modules/`, `dist/`, `*.d.ts`, `components.d.ts`, `auto-imports.d.ts`.
- Nuxt auto-imports components and composables: no import line does not mean unused.
- A `pages/` file reachable by no link, redirect or middleware is not on the flow.
