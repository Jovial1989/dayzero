---
rule: funnel.too_many_clicks
expect: fires
flow_role: first_value
measured: 7
---

```tsx title="app/flow.tsx"
// Primary path, 1 interaction per screen
// 1. Landing: <Link href="/signup">Start</Link>
// 2. Signup: <button type="submit">Create account</button>
// 3. Onboarding: <button>Continue</button>
// 4. Welcome: <button>Next</button>
// 5. Setup: <button>Next</button>
// 6. Dashboard: <button>New item</button>
// 7. Editor: <button>Save</button>  <- first value: the user's item is saved
```
