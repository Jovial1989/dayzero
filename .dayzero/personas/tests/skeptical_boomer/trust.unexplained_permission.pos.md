---
rule: trust.unexplained_permission
expect: fires
measured: false
---

```tsx title="app/onboarding/page.tsx"
export default function Onboarding() {
  return <div>
    <button onClick={() => Notification.requestPermission()}>Continue</button>
  </div>;
}
```
