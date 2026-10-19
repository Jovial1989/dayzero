---
rule: noise.adds_notifications
expect: silent
measured: false
---

```ts title="lib/reports.ts"
export async function scheduleWeeklyReport(userId: string) {
  const data = await buildReport(userId);
  return data; // shown on /reports, nothing is sent
}
```
