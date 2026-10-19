---
rule: pricing.hidden_price
expect: silent
measured: true
---

```tsx title="app/page.tsx"
export default function Landing() {
  return <section>
    <h1>Plan your week in 5 minutes</h1>
    <p>Free, or Pro for $9/month</p>
  </section>;
}
```
