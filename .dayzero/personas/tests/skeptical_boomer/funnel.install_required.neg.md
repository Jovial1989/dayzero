---
rule: funnel.install_required
expect: silent
measured: false
---

```tsx title="app/page.tsx"
export default function Landing() {
  return <section>
    <a href="https://apps.apple.com/app/id000">App Store</a>
    <a href="https://play.google.com/store/apps/details?id=x">Google Play</a>
    <a href="/app">Or open it in your browser</a>  {/* /app is the full web app */}
  </section>;
}
```
