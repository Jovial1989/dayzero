# Stack guide: Next.js and React web (nextjs-react)

Checked: 2026-10-19. Covers Next.js App Router, Pages Router, and React SPAs (Vite, CRA).

## 1. Detection signals

- Strong: `app/layout.(tsx|jsx)` (App Router); `pages/_app.(tsx|jsx)` (Pages Router); `src/main.(tsx|jsx)` or `src/index.(tsx|jsx)` calling `createRoot(`.
- Weak: `package.json` with `next`, `react-dom`, `vite`, or `react-scripts`.

## 2. Entry point

- App Router: `app/page.tsx` is `/`. Layouts wrap pages. `middleware.ts` runs before routes.
- Pages Router: `pages/index.tsx` is `/`.
- SPA: the component passed to `createRoot(...).render(...)`, then the router inside it.

## 3. Screens or commands

- Globs: `app/**/page.(tsx|jsx)`, `pages/**/*.(tsx|jsx)` (not `_app`, `_document`, `api/`), `src/pages/**`, `src/routes/**`, `src/screens/**`, `src/views/**`.
- Route groups `(group)` and dynamic segments `[id]` are part of the URL rules, not separate screens.

## 4. Navigation

- `<Link href>`, `router.push(`, `redirect(`, `useNavigate()`, `<Navigate>`.
- `middleware.ts` / `middleware.js` redirects and `matcher` config; layout-level auth guards.
- React Router: `createBrowserRouter`, `<Routes>`, `<Route path>`.

## 5. Forms and inputs

- `<form>`, `<input required>`, `<select>`, `<textarea>`; libraries `react-hook-form` (`register(..., { required })`), Formik, Zod/Yup schemas.
- Count server checks too: route handlers or server actions that reject a field (e.g. domain or password rules).
- Password + confirm = 2 fields. Hidden inputs never count.

## 6. Auth

- NextAuth/Auth.js (`authOptions`, `providers`), Clerk, Supabase Auth, Firebase Auth, custom `api/auth/*` routes.
- OAuth present only if a provider is configured and a button or route reaches it.
- Verification: pages like `verify-email`, tokens in links, middleware checks on a `verified` flag or cookie.

## 7. Billing

- Stripe (`stripe.checkout.sessions.create`, `payment_method_collection`, `trial_period_days`), Paddle, Lemon Squeezy.
- Plan checks: `plan === 'pro'`, `isPro`, limit constants (e.g. `FREE_TODO_LIMIT`).
- `pricing` page text gives `price_visible` and `lowest_paid_usd_month`.

## 8. Permissions

- `Notification.requestPermission(`, `navigator.geolocation`, `getUserMedia(`, `navigator.clipboard`, `navigator.contacts`.
- An explanation counts if text on the same component renders before the request call.

## 9. User-facing text

- JSX text, `messages/*.json`, `locales/**`, `next-intl`, `i18next` resources, `metadata` exports, README.

## 10. Styles, api, jobs

### styles

- `tailwind.config.*`, `globals.css`, CSS modules, `style={{ fontSize }}`, theme providers (MUI, Chakra).
- Tailwind sizes: `text-xs` 12px, `text-sm` 14px, `text-base` 16px.

### api

- `app/api/**/route.(ts|js)`, `pages/api/**`, server actions (`"use server"`), tRPC routers.
- User-facing API = token or key auth for users, not only session cookies.

### jobs

- Vercel Cron (`vercel.json` `crons`), route handlers called by a scheduler with a secret, Inngest, BullMQ, email senders (Resend, SendGrid, Nodemailer), web push.

## 11. First-value hints

- `first_value`: the first page where the user creates or sees their own item (e.g. a dashboard with a "create" form submitted once).
- `upgrade`: an upsell link, a limit response (HTTP 402, "upgrade"), or a pricing page → Stripe checkout → `plan` updated on success URL or webhook.
- `invite`: invite form or route → email with a signup link carrying a workspace or invite param → invitee lands in the shared workspace.
- `return`: login page or magic link → dashboard with existing data.

## 12. Known traps

- Exclude: `.next/`, `out/`, `node_modules/`, `public/` assets, `*.d.ts`, `next-env.d.ts`, storybook (`*.stories.*`), tests (`*.test.*`, `__tests__/`).
- `"use client"` components are UI, not routes; a page is only what the router maps.
- A page that exists but no link, redirect, or middleware reaches is not on the flow.
- Server action redirects count as navigation.
