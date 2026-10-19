---
rule: pricing.no_free_path
expect: silent
measured: true
---

```tsx title="app/pricing/page.tsx"
const plans = [
  { name: "Free", price: 0, limit: "3 projects", card: false },
  { name: "Pro", price: 12, trial: "14 days, card required" },
];
```
