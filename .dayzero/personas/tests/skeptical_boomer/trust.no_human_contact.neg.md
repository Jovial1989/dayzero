---
rule: trust.no_human_contact
expect: silent
measured: true
---

```tsx title="components/Footer.tsx"
export function Footer() {
  return <footer>
    <a href="/contact">Contact form</a>
    <a href="mailto:support@acme.example">support@acme.example</a>
  </footer>;
}
```
