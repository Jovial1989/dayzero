---
rule: noise.adds_notifications
expect: fires
measured: true
---

```ts title="lib/reports.ts"
export async function scheduleWeeklyReport(userId: string) {
  const data = await buildReport(userId);
  await sendEmail(userId, "Your weekly report", data); // every Monday
}
```
