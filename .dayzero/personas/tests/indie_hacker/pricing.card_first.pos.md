---
rule: pricing.card_first
expect: fires
measured: true
---

```ts title="app/api/signup/route.ts"
export async function POST(req: Request) {
  const user = await createUser(await req.json());
  return redirect(await stripe.checkout.sessions.create({ customer_email: user.email }).url);
}
```
