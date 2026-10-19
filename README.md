# DayZero

**The synthetic crowd engine. Like Reddit, but you own the users.**

Validate your PMF and get Kano Model reports using your own local LLM (Cursor/Claude) without exposing your code.

---

## Why

- AI lets you ship a SaaS in a weekend. It does not tell you if anyone wants it.
- Classic customer development is slow: recruiting, calls, notes.
- DayZero gives you a crowd of hostile, specific, synthetic users on day 0. Inside your IDE.

## What it is

- A `.dayzero/` folder. Markdown instructions + JSON personas.
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

- Executive summary with a ship / fix / kill verdict
- Funnel analysis: which step each persona drops at, and why
- Kano matrix for your 5 core features: Must-have, Performance, Delighter, Indifferent, Reverse
- Top 3 brutal quotes from the synthetic crowd

## How the run works

1. Scan the codebase. Extract 5 value propositions, each tied to file paths.
2. Map the user flow from routes, screens, and forms.
3. Switch to Critic Mode. No praise, no hedging.
4. Load every persona in `.dayzero/personas/`.
5. Walk each persona through the flow. Apply their hard `inference_rule`.
6. Ask each persona the Kano functional and dysfunctional question per feature.
7. Classify with the standard 5×5 Kano table. Compute Better/Worse.
8. Fill `templates/report_template.md`. Nothing more, nothing less.

Full method: [`VISION.md`](VISION.md). Full instructions: [`.dayzero/system_protocol.md`](.dayzero/system_protocol.md).

## Privacy

- The protocol forbids sending code or reports to any URL or API.
- The assistant reads your repo read-only and writes 1 file: the report.
- Your code goes only where your assistant already sends it.

## Community Edition vs Pro

| | Community Edition | Pro Pack |
|---|---|---|
| Protocol + report template | ✓ | ✓ |
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

Copy any file in `.dayzero/personas/`, keep the fields in [`persona.schema.json`](.dayzero/personas/persona.schema.json), and make the `inference_rule` hard enough to hurt.

## Limits

- Synthetic respondents are not customers. Treat the report as a filter, not proof.
- 3 personas = directional signal. Run real interviews before you bet the company.
- Quality depends on the model behind your assistant.

## Contributing

- New personas: open a PR with 1 JSON file in `.dayzero/personas/` that passes `persona.schema.json`.
- Protocol changes: open an issue first and describe the run that went wrong.
