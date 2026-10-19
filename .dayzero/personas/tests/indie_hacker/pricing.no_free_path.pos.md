---
rule: pricing.no_free_path
expect: fires
measured: false
---

```tsx title="app/pricing/page.tsx"
const plans = [
  { name: "Pro", price: 12, trial: "14 days, card required" },
];
```
