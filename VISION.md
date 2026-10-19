# DayZero Vision

> Ship nothing nobody asked for.

DayZero is a movement against dead products. It starts as a folder you drop into your repo.

---

## 1. The Vibe Coding Trap

- AI made code cheap. A full SaaS now takes 1 weekend.
- Validation did not get cheaper. Customer development still means recruiting, scheduling, 30-minute calls, and notes nobody rereads.
- So builders skip it. They ship, post on Show HN, and wait.
- Our working assumption: 8 in 10 of those launches become zombies. Live URL, working Stripe, 0 returning users.
- The bottleneck moved. Writing code is no longer the hard part. Knowing which code deserves to exist is.
- Every hour of vibe coding without a signal is an hour spent building a better tombstone.

## 2. Enter DayZero: PMF inside your IDE

- DayZero is a synthetic crowd engine. Like Reddit, but you own the users.
- No recruiting. No incentives. No "can we hop on a call next Tuesday".
- You get a crowd of opinionated, hard-to-please people who read your product the moment it compiles.
- It solves the cold start problem: feedback on day 0, before the first line of backend exists.
- It also emulates life inside the product: who signs up, where they stall, which step they close the tab on.
- The output is 1 Markdown report. Funnel drop-offs, a Kano matrix, and the 3 quotes that will hurt the most.

What DayZero is not:

- Not a replacement for real users. It is the filter you run before you spend real users.
- Not a PMF certificate. Synthetic signal is directional, and every report says so.

## 3. How It Works: Prompt-as-Software Architecture

- DayZero is not a Python library. It is not a SaaS. It contains 0 lines of executable code.
- It is a set of protocols: a `.dayzero/` directory of Markdown instructions and JSON personas.
- The orchestrator is the AI assistant you already pay for: Cursor, Claude Code, Copilot.

The run, end to end:

1. You type `@.dayzero validate` in your assistant's chat.
2. The assistant reads `system_protocol.md` and follows it as a program.
3. It scans your source code and extracts the 5 value propositions your product actually ships.
4. It maps your user flow from routes, screens, and forms.
5. It loads every persona in `personas/` and walks each one through that flow.
6. It runs a Kano interview per persona per feature.
7. It writes the report into `.dayzero/reports/`, following `templates/report_template.md` exactly.

Why this shape:

- **BYOK, Bring Your Own Key.** The run uses your assistant and your tokens. We never see a request.
- **Zero leak surface.** Your code never leaves the machine and model provider you already trust. There is no DayZero server to breach.
- **Zero install.** Copy a folder. Nothing to `pip install`, nothing to audit, nothing that runs on its own.
- **Forkable.** The program is plain text. Edit a persona, tighten a rule, open a PR.

## 4. The Kano Matrix & Brutal Honesty

The default LLM is a people-pleaser. Ask it about your app and it says "great idea". That answer is worthless.

DayZero personas run in Critic Mode. They are jailbroken out of politeness, not out of safety:

- Praise is banned. Hedging is banned. "It depends" is banned.
- Each persona has a hard `inference_rule` that fires on real product traits. A burned-out PM hits 4 clicks and leaves.
- Personas judge only what the code shows. A feature that exists only in your README does not exist.

Who is in the crowd:

- Tired managers who give you 90 seconds.
- Broke students who close the tab at the word "subscription".
- Conservative boomers who read every permission prompt and trust none of them.

The method is the Kano model, not vibes:

- Every feature gets 2 questions per persona.
  - Functional: "How do you feel if the product has this?"
  - Dysfunctional: "How do you feel if it does not?"
- Each answer is 1 of 5: Like, Expect, Neutral, Tolerate, Dislike.
- The answer pair maps through the standard 5×5 table to a category:

| Category | Meaning |
|---|---|
| Must-have (M) | Missing it kills you. Having it earns nothing. |
| Performance (P) | More is better, linearly. |
| Delighter (A) | Unexpected. Drives word of mouth. |
| Indifferent (I) | Nobody cares. Cut it or stop polishing it. |
| Reverse (R) | Users actively prefer you did not build it. |

- The report shows raw counts and Better/Worse coefficients. Dry numbers, no adjectives.

## 5. Monetization & The Open-Core Model

- **Community Edition, free and open source.** The full protocol, the report template, and 3 base personas. Enough to run the method end to end and learn how it thinks.
- **Pro Pack, paid.** An archive of 50+ hardcore persona profiles across income levels, roles, regions, and tech literacy. Drop them into `personas/` and the same protocol scales up. No license server, no new code.
- Why pay: 3 voices give you a direction. 50+ voices give a product team distributions they can argue about in a roadmap meeting.
- Pricing: on request. Open an issue with the **Pro license request** template.

The deal we offer:

- The method stays open. Anyone can audit how a verdict was reached.
- The crowd is the product. We earn by writing better skeptics, not by locking up your data.

---

Build less. Validate on day 0. Let the crowd kill the bad ideas before your users have to.
