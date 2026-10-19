---
rule: signup.over_two_fields
expect: silent
flow_role: signup
measured: 2
---

```tsx title="app/signup/page.tsx"
export default function SignUp() {
  return (
    <form action="/api/signup" method="post">
      <input name="email" required />
      <input name="password" required />
      <button type="submit">Create account</button>
    </form>
  );
}
```
