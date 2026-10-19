---
rule: trust.no_sso
expect: silent
measured: true
---

```tsx title="app/signup/page.tsx"
<form action="/api/signup" method="post">
  <input name="email" required />
  <input name="password" required />
  <button type="submit">Create account</button>
</form>
<button onClick={() => signIn("google")}>Continue with Google</button>
```

```ts title="auth.ts"
export const { auth, signIn } = NextAuth({ providers: [Google] });
```
