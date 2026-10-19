---
rule: data.no_exit_dislike
expect: silent
measured: true
---

```ts title="app/api/notes/route.ts"
export async function GET() { return Response.json(await db.notes.findMany()); } // session cookie only, UI use
```

```tsx title="app/settings/page.tsx"
<a href="/api/export.csv" download>Export all notes (CSV)</a>
```
