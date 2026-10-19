# Changelog

## Protocol v1.1 (unreleased)

### Added

- `measurements.json`: 24 shared measurements in 6 categories (funnel, auth, pricing, trust, data, ux_noise). Each one defines what to count, where to look, and when a value is `inferred` or `not_applicable`.
- `measurements.schema.json`.
- Persona schema v2: structured `rules` (measurement, comparison, threshold, scope, effect, priority, source, tests, reaction).
- Step 1c measurement sheet: the product is measured once, before personas load. All personas judge the same numbers.
- Rule evaluation with a fixed conflict order: `drop` > `kano_force` > `kano_cap` > `flag`, then priority.
- `validate --test-rules [persona_id]`: checks each rule against its positive and negative test snippets.
- Hard rule R9: no drop or forced answer without a rule behind it.
- Feature traits (ai, team, notifications, data, gamification) and step roles (landing, signup, verify, onboarding, first_screen, first_value, pricing, checkout).
- Report: Glossary, Skipped rules and Untested rules rows; Measurement sheet; rule columns in "Why they left" and Raw answers; Rules fired table; heuristic count in the footer.
- Any-stack support: `.dayzero/stacks/` with guides for `nextjs-react`, `flutter`, `ios-swiftui`, `cli-api`, plus `_generic.md` (stack detection, app discovery, fallback for other stacks, labelled `unknown`).
- `validate --flow <name>`: walk `first_value` (default), `upgrade`, `invite`, or `return`. 8 new step roles for these flows.
- `validate --app <path>`: pick 1 app in a repo with several. Without it, the app with the most user-facing files is auto-picked and the others are listed.
- Flows that cannot be traced in code end in an honest `n/a` report instead of invented steps.
- Report header: Stack, App, Flow, Other apps.

### Changed

- R3: read-only file tools are allowed. Running the project, tests, builds, installs, or anything that writes is not.
- Clicks are always cumulative from the first screen (`clicks_to_value`).
- Survival counts personas who entered a step. A persona who drops at a step counts in that step.
- Weakest feature: a Reverse feature ranks first and shows `R n/N` when Worse is `n/a`.
- Dead-end steps drop every remaining persona with rule id `dead_end`.
- Glossary 1.1: `where_to_look` uses 10 stack-neutral concepts (screen, navigation, form, auth, billing, permission, text, styles, api, jobs).
- When a step has several ways forward, the primary action is walked, never the shorter path.
- Biggest drop-off tie: the earliest tied step is shown and marked as a tie.
- `validate --flow` (v1.0 flow-only report) is renamed `validate --funnel-only`.

### Compatibility

- v1 personas (`inference_rule` only) still run in legacy mode. Their fires are labelled `legacy, unmeasured`.

## Protocol v1.0 (2026-10-19)

- First public release: system protocol, 3 Community Edition personas, Kano report template.
