---
rule: trust.unexplained_permission
expect: silent
measured: true
---

```tsx title="app/onboarding/page.tsx"
export default function Onboarding() {
  return <div>
    <p>We remind you at 9am so you do not miss a day. You can turn it off any time.</p>
    <button onClick={() => Notification.requestPermission()}>Continue</button>
  </div>;
}
```
