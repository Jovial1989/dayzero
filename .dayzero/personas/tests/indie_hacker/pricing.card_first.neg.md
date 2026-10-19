---
rule: pricing.card_first
expect: silent
measured: false
---

```ts title="app/api/signup/route.ts"
export async function POST(req: Request) {
  const user = await createUser(await req.json());
  return redirect("/dashboard"); // checkout only from /pricing later
}
```
