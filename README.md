# DayZero

**The synthetic crowd engine. Like Reddit, but you own the users.**

Validate your PMF and get Kano Model reports using your own local LLM (Cursor/Claude) without exposing your code.

---

## Why

- AI lets you ship a SaaS in a weekend. It does not tell you if anyone wants it.
- Classic customer development is slow: recruiting, calls, notes.
- DayZero gives you a crowd of hostile, specific, synthetic users on day 0. Inside your IDE.

## What it is

- A `.dayzero/` folder. Markdown instructions + JSON data.
- 0 lines of executable code. Nothing to install, nothing that runs by itself.
- Your AI assistant is the runtime. It reads the protocol and executes it on your repo.
- BYOK: your assistant, your tokens, your model provider. DayZero has no server.

## Quick start

**1. Copy the folder**

Put `.dayzero/` in the root of the project you want to validate.

```
your-project/
├── .dayzero/
│   ├── system_protocol.md
│   ├── measurements.json
│   ├── kano_answers.json
│   ├── stacks/
│   ├── personas/
│   ├── templates/
│   └── reports/
├── src/
└── ...
```

**2. Ask your assistant**

In Cursor or Claude Code chat, type:

```
@.dayzero validate
```

If your assistant does not pick up the folder, point it at the entry file:

```
@.dayzero/system_protocol.md validate
```

**3. Read the report**

The assistant writes `.dayzero/reports/dayzero-report-YYYY-MM-DD.md`:

- Executive summary with a SHIP / FIX / KILL verdict
- Funnel analysis: which step each persona drops at, the rule behind it, and the file that caused it
- Kano matrix for your 5 core features, with a quadrant chart
- Kano interview: every persona's answers, plus the few that broke from the crowd
- Top 3 brutal quotes from the synthetic crowd

## Commands

| Command | What it does |
|---|---|
| `@.dayzero validate` | Full run on the new-user flow |
| `@.dayzero validate --flow upgrade` | Walk 1 named flow: `first_value` (default), `upgrade`, `invite`, `return` |
| `@.dayzero validate --app apps/mobile` | In a repo with several apps, test 1 of them |
| `@.dayzero validate --persona tired_pm` | Run with 1 persona |
| `@.dayzero validate --feature "Checkout"` | Kano interview for 1 feature |
| `@.dayzero validate --funnel-only` | Funnel only, no Kano |
| `@.dayzero validate --test-rules` | Check every persona rule against its test snippets |

Flags combine: `@.dayzero validate --app apps/web --flow invite`.

## Supported stacks

| Stack | Detected by |
|---|---|
| Next.js and React web | `app/layout.tsx`, `pages/_app.tsx`, or `createRoot(` |
| Flutter | `lib/main.dart` with `runApp(` |
| iOS SwiftUI | `@main` type conforming to `App` |
| CLI tools and backend APIs | `bin` in `package.json`, `[project.scripts]`, Go `main` with cobra, or a server entry |

- Anything else runs on a generic guide and the report says `Stack: unknown`.
- In a monorepo, the app with the most screens is picked and the others are listed with a ready `--app` command.
- If a flow is not in the code, the report says so instead of inventing steps.
- Stack knowledge lives in `.dayzero/stacks/`, 1 Markdown file per stack.

## How the run works

1. Detect the stack and the app. Load the matching guide from `.dayzero/stacks/`.
2. Extract 5 value propositions, each tied to file paths.
3. Map the requested flow (new user, upgrade, invite, return), step by step, from the code.
4. Measure the product once: clicks to value, form fields, OAuth, price, permissions, contrast, and 18 more, from `measurements.json`.
5. Switch to Critic Mode. No praise, no hedging.
6. Walk every persona through the flow. Their rules fire on the measured values.
7. Interview every persona with the Kano functional and dysfunctional question per feature. Answers come from 1 fixed list of 5 lines.
8. Only where a persona breaks from the crowd or from its own profile does it answer in its own words.
9. Classify with the standard 5×5 Kano table. Compute Better/Worse. Plot the quadrant.
10. Fill `templates/report_template.md`. Nothing more, nothing less.

Full method: [`VISION.md`](VISION.md). Full instructions: [`.dayzero/system_protocol.md`](.dayzero/system_protocol.md).

## The Kano quadrant

The report draws your 5 features on 2 axes:

- **Up:** how much a feature delights when it is there (Better).
- **Right:** how much its absence hurts (|Worse|).

| | Absence hurts little | Absence hurts a lot |
|---|---|---|
| **Presence delights** | Delighter | Performance |
| **Presence does not delight** | Indifferent | Must-have |

GitHub renders the chart from a Mermaid block. Every other viewer gets the same result as a table.

## Privacy

- The protocol forbids sending code or reports to any URL or API.
- The assistant reads your repo read-only and writes 1 file: the report.
- Your code goes only where your assistant already sends it.

## Community Edition vs Pro

| | Community Edition | Pro Pack |
|---|---|---|
| Protocol, stack guides, report template | ✓ | ✓ |
| Personas | 3 base profiles | 50+ hardcore profiles |
| Report confidence label | directional | indicative to broad |
| Price | free, open source | on request |

**Community Edition** ships 3 personas:

- `indie_hacker.json`: solo founder, 0 patience for setup
- `tired_pm.json`: burned-out PM, leaves after 3 clicks
- `skeptical_boomer.json`: conservative buyer, distrusts every data prompt

**Pro Pack** is an archive of 50+ profiles in the same schema. Unzip into `.dayzero/personas/`. Same protocol, wider crowd, real distributions.

To get Pro: open an issue with the **Pro license request** template.

## Write your own persona

A persona is 1 JSON file in `.dayzero/personas/` that passes [`persona.schema.json`](.dayzero/personas/persona.schema.json).

Its behaviour comes from `rules`. Each rule:

- names 1 measurement from [`measurements.json`](.dayzero/measurements.json) (for example `form_fields` or `clicks_to_value`)
- compares it to a threshold (`form_fields > 3`) or a true/false check (`oauth_present is false`)
- applies at a step, a kind of feature, or everywhere
- has 1 effect: `drop` (the persona leaves), `kano_force` or `kano_cap` (sets or limits a Kano answer), or `flag`
- carries a source for its threshold (public research, your own interviews with sample size, or `heuristic`)
- comes with 2 test snippets in `personas/tests/<persona_id>/`: 1 where it must fire, 1 where it must stay silent

Check your rules with `@.dayzero validate --test-rules`.

Personas written for v1.0 (a free-text `inference_rule`) still run. Their results are labelled `legacy, unmeasured`.

## Limits

- Synthetic respondents are not customers. Treat the report as a filter, not proof.
- 3 personas = directional signal. Run real interviews before you bet the company.
- Quality depends on the model behind your assistant.
- The 3 bundled personas still use the v1.0 free-text format, so Kano answers vary between runs. Personas with structured rules are more stable.

## Contributing

- New personas: open a PR with 1 JSON file in `.dayzero/personas/` that passes `persona.schema.json`, plus its rule tests.
- New stacks: open a PR with 1 guide in `.dayzero/stacks/` that follows the 12 sections of `_generic.md`.
- Protocol changes: open an issue first and describe the run that went wrong.
