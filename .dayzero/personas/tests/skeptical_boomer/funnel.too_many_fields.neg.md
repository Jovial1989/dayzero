---
rule: funnel.too_many_fields
expect: silent
flow_role: signup
measured: 5
---

```tsx title="app/signup/page.tsx"
export default function SignUp() {
  return (
    <form action="/api/signup" method="post">
      <input name="email" required />
      <input name="password" required />
      <input name="name" required />
      <input name="company" required />
      <input name="phone" required />
      <button type="submit">Create account</button>
    </form>
  );
}
```
