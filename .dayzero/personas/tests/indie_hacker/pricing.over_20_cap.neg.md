---
rule: pricing.over_20_cap
expect: silent
measured: 20
---

```tsx title="app/pricing/page.tsx"
const plans = [{ name: "Free", price: 0 }, { name: "Pro", price: 20, per: "month" }];
```
