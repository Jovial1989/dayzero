---
rule: onboarding.empty_first_screen
expect: fires
flow_role: first_screen
measured: true
---

```tsx title="app/dashboard/page.tsx"
if (projects.length === 0) return <div>
  <p>No projects yet</p>
  <button>New project</button>
</div>;
```
