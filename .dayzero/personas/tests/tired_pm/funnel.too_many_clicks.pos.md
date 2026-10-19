---
rule: funnel.too_many_clicks
expect: fires
flow_role: first_value
measured: 4
---

```tsx title="app/flow.tsx"
// Primary path, 1 interaction per screen
// 1. Landing: <Link href="/signup">Start</Link>
// 2. Signup: <button type="submit">Create account</button>
// 3. Onboarding: <button>Continue</button>
// 4. Editor: <button>Save</button>  <- first value: the user's item is saved
```
