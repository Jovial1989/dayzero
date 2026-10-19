---
rule: data.no_exit_dislike
expect: fires
measured: false
---

```ts title="app/api/notes/route.ts"
export async function GET() { return Response.json(await db.notes.findMany()); } // session cookie only, UI use
```
