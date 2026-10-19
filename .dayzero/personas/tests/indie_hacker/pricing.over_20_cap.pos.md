---
rule: pricing.over_20_cap
expect: fires
measured: 29
---

```tsx title="app/pricing/page.tsx"
const plans = [{ name: "Free", price: 0 }, { name: "Pro", price: 29, per: "month" }];
```
