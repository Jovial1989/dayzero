# Stack guide: Generic (_generic)

Checked: 2026-10-19. Always loaded. Holds stack detection and app discovery, plus a stack-neutral concept map used when no stack guide matches.

## 1. Detection signals

### Precedence (first match wins; a strong signal beats a weak one at any order)

| Order | Stack id | Strong signal (entry point) | Weak signal (manifest) |
|---|---|---|---|
| 1 | `flutter` | `lib/main.dart` containing `runApp(` | `pubspec.yaml` with a `flutter:` section |
| 2 | `ios-swiftui` | a `.swift` file with `@main` on a type conforming to `App` | `*.xcodeproj` or `Package.swift` with an iOS platform |
| 3 | `nextjs-react` | `app/layout.(tsx\|jsx)`, `pages/_app.(tsx\|jsx)`, or `src/main.(tsx\|jsx)` calling `createRoot(` | `package.json` with `next` or `react-dom` |
| 4 | `cli-api` | `bin` in `package.json`; `[project.scripts]` in `pyproject.toml`; Go `func main()` using `cobra` or `flag`; a server entry (`app.listen(`, `FastAPI(`, `http.ListenAndServe(`) with no UI folder | `package.json`, `pyproject.toml`, or `go.mod` alone |
| 5 | `unknown` | none of the above | any other manifest (`build.gradle*`, `AndroidManifest.xml`, `mix.exs`, `Gemfile`, `manage.py`, …) |

Cite every signal file found in the report.

### App discovery

1. Candidates: the repo root and every folder up to 3 levels deep with its own manifest.
2. App = candidate with a strong signal. Candidate with only a manifest = library, never picked. A candidate inside another app's folder (for example `server/` inside a CLI app) is part of that app, not a separate app; a repo root with no strong signal of its own is not an app.
3. 1 app: test it. 0 apps: treat the root as 1 app with stack `unknown`.
4. More than 1 app and no `--app`: count files matching the app's guide globs for screen, navigation, form (for `cli-api`: command and route handlers). Highest wins. Tie: alphabetically first path, noted as a tie.
5. `--app <path>` must name an app from step 2; otherwise stop and list the apps.

## 2. Entry point

Start from the strong signal file. Follow what it renders, registers, or dispatches first. That first screen or command is the start of `first_value`.

## 3. Screens or commands

- Folders named `pages`, `screens`, `views`, `routes`, `templates`, `commands`, `cmd`.
- Files whose main export renders UI or handles 1 command.

## 4. Navigation

- Router configs, route tables, redirects, guards, middleware, deep-link handlers.
- For a CLI: the command tree (subcommands) and what each command tells the user to run next.

## 5. Forms and inputs

- Input elements, form widgets, prompts, argument parsers.
- Count required inputs from client validation and server validation together.

## 6. Auth

- Sign-up and sign-in screens, session or token storage, verification links, OAuth or SSO config, API key creation.

## 7. Billing

- Pricing pages, plan checks, paywalls, checkout or purchase calls, subscription flags.

## 8. Permissions

- Calls that request device or data access, and platform manifests listing permissions.
- An explanation counts only if it is shown before the request on the same screen.

## 9. User-facing text

- UI strings, i18n files, help output, README and docs.

## 10. Styles, api, jobs

### styles

- Theme files, global styles, design tokens, inline font sizes and colors.

### api

- HTTP route handlers, RPC definitions, public API docs, token-protected endpoints.

### jobs

- Cron, queues, schedulers, email or push senders, webhooks.

## 11. First-value hints

- `first_value`: the first screen or output where the user gets the product's core result (an item created, a result shown, a URL live).
- `upgrade`: first upsell or limit message → payment → paid flag.
- `invite`: invite screen or command → invite link handling → invitee sees shared content.
- `return`: deep link, email link, push, or re-run with stored credentials → back at the user's own data.

## 12. Known traps

- Exclude: `node_modules`, `vendor`, `build`, `dist`, `.next`, `DerivedData`, `Pods`, generated code (`*.g.*`, `*.generated.*`, `*_pb.*`, files with a "generated, do not edit" header).
- Storybook stories, tests, and mocks look like screens but are not part of the flow.
- With stack `unknown`, mark any value you cannot locate with these hints as `inferred`.
