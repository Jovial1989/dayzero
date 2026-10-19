<!--
DayZero report template v1.2
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
| Guides | [each loaded guide with role and concepts owned, e.g. "electron (primary): permission, jobs, auth, billing · nextjs-react (ui): screen, navigation, form, text, styles"; left-out guide if any] |
| App | [path, or "path (auto-picked)", or "path (auto-picked, tie)"] |
| Flow | [first_value / upgrade / invite / return] |
| Other apps | [per app: "path (stack_id): @.dayzero validate --app path", or "none"] |
| Assistant / model | [e.g. Cursor + claude-sonnet-5-5] |
| Protocol | DayZero System Protocol v1.2 |
| Glossary | [version from measurements.json; add "+ pro [version]" when measurements.pro.json is loaded] |
| Answer list | [version from kano_answers.json] |
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

| Feature | M | P | A | I | R | Q | Category | Majority | Better | Worse |
|---|---|---|---|---|---|---|---|---|---|---|
| F1 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [code or none] | [0.00] | [-0.00] |
| F2 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [ ] | [0.00] | [-0.00] |
| F3 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [ ] | [0.00] | [-0.00] |
| F4 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [ ] | [0.00] | [-0.00] |
| F5 [name] | [n] | [n] | [n] | [n] | [n] | [n] | [category] | [ ] | [0.00] | [-0.00] |

<!-- Better = (A+P)/(A+P+M+I). Worse = -(P+M)/(A+P+M+I). Tie-break M > P > A > I > R; mark "split". Majority = most frequent code, Q excluded; tie = none. -->

### Quadrant

<!-- 1 point per feature with numeric coefficients: "F#: [x, y]" with x = |Worse| and y = Better, 0 to 1. Write 1 as "1" and every other value with 2 decimals ("0.00", "0.50"): Mermaid rejects "1.00". The square brackets in point lines are Mermaid syntax and stay in the report. Point names F1 to F5 only. Do not edit the axis, quadrant, or title lines. -->

```mermaid
quadrantChart
    title Kano quadrant
    x-axis Low dissatisfaction if missing --> High dissatisfaction if missing
    y-axis Low satisfaction if present --> High satisfaction if present
    quadrant-1 Performance
    quadrant-2 Delighter
    quadrant-3 Indifferent
    quadrant-4 Must-have
    F1: [x, y]
    F2: [x, y]
```

| | Low dissatisfaction if missing (<0.5) | High dissatisfaction if missing (≥0.5) |
|---|---|---|
| **High satisfaction if present (≥0.5)** | Delighter (Attractive): [F# or none] | Performance (Satisfier): [F# or none] |
| **Low satisfaction if present (<0.5)** | Indifferent: [F# or none] | Must-have (Basic): [F# or none] |

Off chart: [F# Reverse, R n/N · F# Questionable, Q n/N, or "none"]
Quadrant ≠ category: [F# (quadrant X, category Y), or "none"]

### By category

- **Must-have (Basic):** [features, or "none"]. [1 statement on what breaks if missing]
- **Performance (Satisfier):** [features, or "none"]. [1 statement on where more is better]
- **Delighter (Attractive):** [features, or "none"]. [1 statement on why it surprises]
- **Indifferent:** [features, or "none"]. [1 statement: cut or freeze]
- **Reverse:** [features, or "none"]. [1 statement on who it repels and why]
- **Questionable / split:** [features, or "none"]

### Interview

<!-- 1 block per feature F1 to F5. Functional and Dysfunctional cells contain exactly 1 line from kano_answers.json, word for word. Note is empty, or "rule <id>", or trigger tags + 1 quoted custom answer (≤25 words). Never both a rule id and a custom answer. Personas who dropped before the feature: "(dropped at step n)" after the id. -->

#### F1 [name]

**Functional:** If [product] has [feature], how do you feel?
**Dysfunctional:** If [product] does not have [feature], how do you feel?

| Persona | Functional | Dysfunctional | Code | Note |
|---|---|---|---|---|
| [id] | [answer line] | [answer line] | [M/P/A/I/R/Q] | [empty / rule id / `[trigger]` "custom answer"] |
| [id] | [ ] | [ ] | [ ] | [ ] |

#### F2 [name]

[same block]

### Deviations

| Persona | Feature | Code | Majority | Triggers | Custom answer |
|---|---|---|---|---|---|
| [id] | [F#] | [code] | [code or none] | [contradictory / against_crowd / against_bias] | "[custom answer]" |

<!-- 1 row per custom answer in the Interview, or a single row "none". -->

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

<sub>Generated locally by DayZero. Code was read by your assistant only. [N] synthetic personas, confidence: [label]. [k] of [m] fired rules have a heuristic source. [c] custom answers out of [r] interview rows. Run real interviews before betting on these numbers.</sub>
