---
rule: pricing.hidden_price
expect: fires
measured: false
---

```tsx title="app/page.tsx"
export default function Landing() {
  return <section>
    <h1>Plan your week in 5 minutes</h1>
    <a href="mailto:sales@acme.example">Contact sales for pricing</a>
  </section>;
}
```
