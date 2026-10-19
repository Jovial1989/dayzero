<!--
DayZero report template v1.0
The assistant replaces every [ ] with real values and deletes all HTML comments.
Do not add, drop, or reorder sections. Empty data = "n/a: <reason>".
-->

# DayZero Report: [Product name]

| | |
|---|---|
| Date | [YYYY-MM-DD] |
| Repo | [repo folder name] |
| Assistant / model | [e.g. Cursor + claude-sonnet-5-5] |
| Protocol | DayZero System Protocol v1.0 |
| Personas (N) | [N] ([comma-separated persona ids]) |
| Confidence | [directional / indicative / broad] |
| Areas scanned | [e.g. app/routes, components, api; sampled: yes/no] |
| Skipped personas | [ids + reason, or "none"] |

> Synthetic respondents. This report is a directional filter, not customer research and not proof of product-market fit.

---

## 1. Executive Summary

**Verdict: [SHIP / FIX / KILL]**

- **What the product is, per the code:** [1 statement]
- **Reached first value:** [k] of [N] personas ([%])
- **Biggest drop-off:** step [n], [step name]. [k] of [N] personas left here.
- **Strongest feature:** [F#, name], [Kano category], Better [0.00]
- **Weakest feature:** [F#, name], [Kano category], Worse [-0.00]
- **Fix first:** [1 concrete change, tied to a file path]
- **Stop building:** [feature or "n/a"]

### Extracted value propositions

| ID | Feature | Value proposition | Evidence | Clicks to reach | Requires |
|---|---|---|---|---|---|
| F1 | [name] | [what the user gets] | `[path]` | [n] | [signup / payment / permissions / none] |
| F2 | [name] | [what the user gets] | `[path]` | [n] | [ ] |
| F3 | [name] | [what the user gets] | `[path]` | [n] | [ ] |
| F4 | [name] | [what the user gets] | `[path]` | [n] | [ ] |
| F5 | [name] | [what the user gets] | `[path]` | [n] | [ ] |

**Claimed but not built:** [features found in docs/comments with no implementing code, or "none"]

---

## 2. Funnel Analysis (User Flow drop-offs)

### Flow as built

| Step | Screen / route | Evidence | Clicks | Fields | Friction |
|---|---|---|---|---|---|
| 1 | [name] | `[path]` | [n] | [n] | [paywall / permission / empty state / none] |
| 2 | [name] | `[path]` | [n] | [n] | [ ] |
| 3 | [name] | `[path]` | [n] | [n] | [ ] |
| 4 | [name] | `[path]` | [n] | [n] | [ ] |
| [n] | [first value] | `[path]` | [n] | [n] | [ ] |

### Survival

| Step | Personas still in | Survival | Dropped here |
|---|---|---|---|
| 1 | [k] / [N] | [100%] | [ids or "none"] |
| 2 | [k] / [N] | [%] | [ ] |
| 3 | [k] / [N] | [%] | [ ] |
| 4 | [k] / [N] | [%] | [ ] |
| [n] | [k] / [N] | [%] | [ ] |

### Why they left

| Persona | Dropped at | Rule that fired | Evidence | In their words |
|---|---|---|---|---|
| [name] (`[id]`) | step [n] | [inference_rule / secondary rule / deal breaker] | `[path]` | "[quote]" |
| [name] (`[id]`) | [step n / reached first value] | [ ] | `[path]` | "[quote]" |

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

| Persona | Feature | Functional | Dysfunctional | Code | Reason (≤15 words) |
|---|---|---|---|---|---|
| [id] | F1 | [Like/Expect/Neutral/Tolerate/Dislike] | [ ] | [M/P/A/I/R/Q] | [reason] |
| [id] | F2 | [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 4. Top 3 Brutal Quotes

> "[quote 1]"
> **[persona name]** (`[id]`), at [step / feature]

> "[quote 2]"
> **[persona name]** (`[id]`), at [step / feature]

> "[quote 3]"
> **[persona name]** (`[id]`), at [step / feature]

---

<sub>Generated locally by DayZero. Code was read by your assistant only. [N] synthetic personas, confidence: [label]. Run real interviews before betting on these numbers.</sub>
