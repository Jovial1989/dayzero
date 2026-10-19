# Stack guide: CLI tools and backend APIs (cli-api)

Checked: 2026-10-19. Covers command-line tools (Node, Python, Go) and backend-only APIs. Also loaded alongside another guide for the concepts `api` and `jobs` when an app has a server folder.

## 1. Detection signals

- Strong (CLI): `"bin"` in `package.json`; `[project.scripts]` or `entry_points` in `pyproject.toml`/`setup.cfg`; Go `func main()` with `cobra.Command` or `flag.Parse()`.
- Strong (API): a server entry with `app.listen(`, `FastAPI(`, `Flask(`, `http.ListenAndServe(`, `express()` and no UI folder.
- Weak: `package.json`, `pyproject.toml`, or `go.mod` alone.

## 2. Entry point

- CLI: the `bin` file or script target → the command parser → the default or first documented command.
- API: the server entry → mounted routers. The README's quickstart names the first call.

## 3. Screens or commands

- A "screen" is 1 command's output or 1 API response a user reads.
- Globs: `bin/*`, `src/commands/**`, `cmd/**`, `cli/**`, `**/commands/*.py`; API: `routes/**`, `handlers/**`, `controllers/**`, `server/routes/**`, `api/**`.

## 4. Navigation

- Command tree: `program.command(`, `commander`, `yargs.command(`, `click.group`/`@click.command`, `argparse` subparsers, `cobra.Command{Use:}`.
- What a command prints as the next step ("Run `x deploy` next") is navigation.
- API: route registration (`router.get(`, `@app.post(`), middleware order, auth guards.

## 5. Forms and inputs

- Interactive prompts (`inquirer`, `prompts`, `@clack/prompts`, `readline`, `click.prompt`, `survey`) = 1 field per required prompt.
- Required flags or arguments (`requiredOption`, `required=True`, positional args) = 1 field each.
- Request body validation (Zod, Joi, Pydantic) for APIs.

## 6. Auth

- Device-code or browser login (prints URL + code, polls): `oauth_present` is true only if the approval page signs in through a third party (GitHub, Google, SSO). The user approving on the product's own page is 1 click, not `wait_required`; `wait_required` is true only if approval needs someone else (an admin, an email link).
- Token storage (`conf`, `keytar`, `~/.config/<tool>`, env vars) lets `return` skip `signin`.
- User-created API keys or tokens (`apiKeys` routes) = `api_present`.

## 7. Billing

- Server routes calling Stripe/Paddle; plan checks in API handlers (`plan !== 'pro'` → 402); CLI commands that refuse on the free plan.
- README or docs pricing text gives `price_visible` and `lowest_paid_usd_month`.

## 8. Permissions

- CLI: OS-level prompts only (keychain access, macOS privacy prompts for files outside the project). Opening a browser for login is not a permission.
- API: OAuth scopes requested from the user.

## 9. User-facing text

- `--help` text, `.description(`, `console.log`/`print` messages in command files, error messages, README, `docs/`.

## 10. Styles, api, jobs

### styles

- `min_body_font_px`, `low_contrast_text`, `empty_state_without_sample`: always `not_applicable` for a CLI or API. Never infer a terminal font size. Terminal colors (`chalk`, `rich`) do not count as contrast.

### api

- Every route a user or client can call with their own credentials. Public = documented or token-auth for users.

### jobs

- `cron`, `node-cron`, queues (BullMQ, Celery, Sidekiq), `jobs/**`, `workers/**`, email senders, webhook dispatchers.

## 11. First-value hints

- `first_value` (CLI): install (README) = `landing` → setup command(s) = `onboarding` → login = `signup` → the command that prints the core result (a URL, a file, a report) = `first_value`.
- `first_value` (API): get a key = `landing`/`signup` → first documented call → first useful response = `first_value`.
- `upgrade`: a command or response that hits a plan limit → checkout URL → plan active on next call.
- `return`: re-run with stored token = `reentry` → token check (`signin` if expired) → a status or history command = `resume_value`.

## 12. Known traps

- Exclude: `node_modules/`, `dist/`, `build/`, `__pycache__/`, `.venv/`, `vendor/`, generated clients (`*_pb2.py`, `*.pb.go`, `openapi-generated/`), tests.
- Each command run counts as 1 click; each answered prompt counts as 1; approving in the browser counts as 1.
- Internal admin routes are not user-facing API.
