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
- Report: Glossary, Skipped rules and Untested rules rows; Measurement sheet; rule columns in "Why they left"; Rules fired table; heuristic count in the footer.
- Any-stack support: `.dayzero/stacks/` with guides for `nextjs-react`, `flutter`, `ios-swiftui`, `cli-api`, plus `_generic.md` (stack detection, app discovery, fallback for other stacks, labelled `unknown`).
- `validate --flow <name>`: walk `first_value` (default), `upgrade`, `invite`, or `return`. 8 new step roles for these flows.
- `validate --app <path>`: pick 1 app in a repo with several. Without it, the app with the most user-facing files is auto-picked and the others are listed.
- Flows that cannot be traced in code end in an honest `n/a` report instead of invented steps.
- Report header: Stack, App, Flow, Other apps.
- Kano interview mode: `kano_answers.json` holds 1 shared set of 5 standard answer lines ("I like it that way." to "I dislike it that way."). Every persona picks from it, word for word.
- 2-pass interview: pass 1 collects answers only; pass 2 writes a custom answer (≤25 words, persona voice) only when a row is `contradictory` (Q), `against_crowd` (opposite to the feature's majority), or `against_bias` (opposite to the persona's own `kano_bias`).
- Kano quadrant in the report: a Mermaid `quadrantChart` of Better against |Worse| (Delighter, Performance, Indifferent, Must-have), with a text fallback table.
- Report Section 3: Majority column, Interview grouped by feature, Deviations table, custom-answer count in the footer.

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
- Raw answers table replaced by the Interview. The per-pair free-text reason is gone.
- Top 3 quotes come only from drop reactions and custom answers.

### Compatibility

- v1 personas (`inference_rule` only) still run in legacy mode. Their fires are labelled `legacy, unmeasured`.

## Protocol v1.0 (2026-10-19)

- First public release: system protocol, 3 Community Edition personas, Kano report template.
