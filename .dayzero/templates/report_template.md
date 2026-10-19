<!--
DayZero report template v1.1
The assistant replaces every [ ] with real values and deletes all HTML comments.
Do not add, drop, or reorder sections. Empty data = "n/a: <reason>".
Flow not traceable or not found: Section 1 verdict = that n/a; Sections 2 and 3 = n/a + what was searched + other flows found; Section 4 = n/a.
-->

# DayZero Report: [Product name]

| | |
|---|---|
| Date | [YYYY-MM-DD] |
| Repo | [repo folder name] |
| Stack | [stack_id + signal file, or "unknown (generic guide)"] |
| App | [path, or "path (auto-picked)", or "path (auto-picked, tie)"] |
| Flow | [first_value / upgrade / invite / return] |
| Other apps | [per app: "path (stack_id): @.dayzero validate --app path", or "none"] |
| Assistant / model | [e.g. Cursor + claude-sonnet-5-5] |
| Protocol | DayZero System Protocol v1.1 |
| Glossary | [version from measurements.json] |
| Personas (N) | [N] ([comma-separated persona ids]; mark legacy ones `(legacy)`) |
| Confidence | [directional / indicative / broad] |
| Areas scanned | [e.g. app/routes, components, api; sampled: yes/no] |
| Skipped personas | [ids + reason, or "none"] |
| Skipped rules | [persona_id:rule_id + reason, or "none"] |
| Untested rules | [persona_id:rule_id, or "none"] |

> Synthetic respondents. This report is a directional filter, not customer research and not proof of product-market fit.

---

## 1. Executive Summary

**Verdict: [SHIP / FIX / KILL]**

- **What the product is, per the code:** [1 statement]
- **Reached first value:** [k] of [N] personas ([%])
- **Biggest drop-off:** step [n], [step name]. [k] of [N] personas left here. Main rule: `[rule id]`. [If tied: "Tie with steps [x, y]; earliest shown."]
- **Strongest feature:** [F#, name], [Kano category], Better [0.00]
- **Weakest feature:** [F#, name], [Kano category], [Worse -0.00, or R n/N if Reverse]
- **Fix first:** [1 concrete change, tied to a file path]
- **Stop building:** [feature or "n/a"]

### Extracted value propositions

| ID | Feature | Value proposition | Evidence | Clicks to reach | Requires | Traits |
|---|---|---|---|---|---|---|
| F1 | [name] | [what the user gets] | `[path]` | [n] | [signup / payment / permissions / none] | [ai, team, notifications, data, gamification, or none] |
| F2 | [name] | [what the user gets] | `[path]` | [n] | [ ] | [ ] |
| F3 | [name] | [what the user gets] | `[path]` | [n] | [ ] | [ ] |
| F4 | [name] | [what the user gets] | `[path]` | [n] | [ ] | [ ] |
| F5 | [name] | [what the user gets] | `[path]` | [n] | [ ] | [ ] |

**Claimed but not built:** [features found in docs/comments with no implementing code, or "none"]

---

## 2. Funnel Analysis (User Flow drop-offs)

### Flow as built

| Step | Screen / route | Role | Evidence | Friction |
|---|---|---|---|---|
| 1 | [name] | [landing] | `[path]` | [paywall / permission / empty state / dead end / none] |
| 2 | [name] | [signup] | `[path]` | [ ] |
| 3 | [name] | [ ] | `[path]` | [ ] |
| 4 | [name] | [ ] | `[path]` | [ ] |
| [n] | [first value] | first_value | `[path]` | [ ] |

### Measurement sheet

<!-- 1 row per glossary measurement per level target. Product-level measurements: 1 row each. -->

| Measurement | Level | Step / feature | Value | Status | Evidence |
|---|---|---|---|---|---|
| [clicks_to_value] | step | [step n] | [n] | [measured / inferred / not_applicable] | `[path]` |
| [form_fields] | step | [step n] | [n] | [ ] | `[path]` |
| [oauth_present] | product | product | [true / false] | [ ] | `[path]` |
| [ ] | [ ] | [ ] | [ ] | [ ] | `[ ]` |

### Survival

| Step | Entered step | Survival | Dropped here |
|---|---|---|---|
| 1 | [k] / [N] | [100%] | [ids or "none"] |
| 2 | [k] / [N] | [%] | [ ] |
| 3 | [k] / [N] | [%] | [ ] |
| 4 | [k] / [N] | [%] | [ ] |
| [n] | [k] / [N] | [%] | [ ] |

### Why they left

| Persona | Dropped at | Rule id | Measurement | Threshold | Measured | Evidence | In their words |
|---|---|---|---|---|---|---|---|
| [name] (`[id]`) | step [n] | `[rule id / legacy / dead_end]` | [measurement] | [comparison + threshold] | [value / unmeasured] | `[path]` | "[quote]" |
| [name] (`[id]`) | [step n / reached first value] | `[ ]` | [ ] | [ ] | [ ] | `[path]` | "[quote]" |

---

## 3. Kano Matrix

### Classification

| Feature | M | P | A | I | R | Q | Category | Better | Worse |
|---|---|---|---|---|---|---|---|---|---|
| F1 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [0.00] | [-0.00] |
| F2 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [0.00] | [-0.00] |
| F3 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [0.00] | [-0.00] |
| F4 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [0.00] | [-0.00] |
| F5 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [0.00] | [-0.00] |

<!-- Better = (A+P)/(A+P+M+I). Worse = -(P+M)/(A+P+M+I). Tie-break M > P > A > I > R; mark "split". -->

### By category

- **Must-have:** [features, or "none"]. [1 statement on what breaks if missing]
- **Performance:** [features, or "none"]. [1 statement on where more is better]
- **Delighters:** [features, or "none"]. [1 statement on why it surprises]
- **Indifferent:** [features, or "none"]. [1 statement: cut or freeze]
- **Reverse:** [features, or "none"]. [1 statement on who it repels and why]
- **Questionable / split:** [features, or "none"]

### Raw answers

| Persona | Feature | Functional | Dysfunctional | Code | Rule | Reason (≤15 words) |
|---|---|---|---|---|---|---|
| [id] | F1 | [Like/Expect/Neutral/Tolerate/Dislike] | [ ] | [M/P/A/I/R/Q] | `[rule id or none]` | [reason] |
| [id] | F2 | [ ] | [ ] | [ ] | `[ ]` | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] | `[ ]` | [ ] |

### Rules fired

| Persona | Rule id | Effect | Scope | Measured vs threshold | State | Source type |
|---|---|---|---|---|---|---|
| [id] | `[rule id]` | [drop / kano_force / kano_cap / flag] | [step role / feature trait / global] | [4 > 3] | [applied / overridden / flag only] | [public / own / heuristic / legacy] |
| [ ] | `[ ]` | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 4. Top 3 Brutal Quotes

> "[quote 1]"
> **[persona name]** (`[id]`), at [step / feature]

> "[quote 2]"
> **[persona name]** (`[id]`), at [step / feature]

> "[quote 3]"
> **[persona name]** (`[id]`), at [step / feature]

---

<sub>Generated locally by DayZero. Code was read by your assistant only. [N] synthetic personas, confidence: [label]. [k] of [m] fired rules have a heuristic source. Run real interviews before betting on these numbers.</sub>
