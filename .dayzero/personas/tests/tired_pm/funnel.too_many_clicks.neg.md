---
rule: funnel.too_many_clicks
expect: silent
flow_role: first_value
measured: 3
---

```tsx title="app/flow.tsx"
// Primary path, 1 interaction per screen
// 1. Landing: <Link href="/signup">Start</Link>
// 2. Signup: <button type="submit">Create account</button>
// 3. Editor: <button>Save</button>  <- first value: the user's item is saved
```
