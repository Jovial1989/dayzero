---
rule: trust.no_sso
expect: fires
measured: false
---

```tsx title="app/signup/page.tsx"
<form action="/api/signup" method="post">
  <input name="email" required />
  <input name="password" required />
  <button type="submit">Create account</button>
</form>
```
