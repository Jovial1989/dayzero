---
rule: onboarding.empty_first_screen
expect: silent
flow_role: first_screen
measured: false
---

```tsx title="app/dashboard/page.tsx"
if (projects.length === 0) return <div>
  <p>No projects yet</p>
  <button>New project</button>
  <button onClick={createSampleProject}>Start from a sample project</button>
</div>;
```
