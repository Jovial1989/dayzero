# Stack guide: iOS SwiftUI (ios-swiftui)

Checked: 2026-10-19. Covers SwiftUI apps for iOS 16+ (UIKit screens are read the same way through view controllers).

## 1. Detection signals

- Strong: a `.swift` file with `@main` on a type conforming to `App` (`@main struct X: App`).
- Weak: `*.xcodeproj`, `*.xcworkspace`, or `Package.swift` with `.iOS(` platform.

## 2. Entry point

- The `@main` App's `body` → `WindowGroup { RootView() }`. Root views often switch on state (onboarded, signed in).
- `.onOpenURL` and `UNUserNotificationCenterDelegate` on the App or a delegate are entry points for `return`.

## 3. Screens or commands

- Globs: `**/Views/**/*.swift`, `**/Screens/**/*.swift`, `**/*View.swift`, `**/*Screen.swift`; UIKit `*ViewController.swift`.
- A screen is a `View` used as a navigation destination, sheet, full-screen cover, or root branch.

## 4. Navigation

- `NavigationStack`, `NavigationLink`, `.navigationDestination(for:)`, `path.append(`.
- `.sheet(`, `.fullScreenCover(`, `TabView`, root `if/switch` on app state.
- Deep links: `.onOpenURL`, URL schemes in `Info.plist` (`CFBundleURLTypes`), universal links.

## 5. Forms and inputs

- `TextField`, `SecureField`, `Picker`, `Toggle` inside `Form` or stacks.
- Required = a submit button disabled until the field is valid, or a validation error on submit.
- Swipe between `TabView(.page)` onboarding pages = 1 click each.

## 6. Auth

- `AuthenticationServices` (`SignInWithAppleButton`, `ASAuthorizationController`) = OAuth present.
- Firebase Auth, Supabase, custom service classes; `LocalAuthentication` (Face ID) for unlocking, not sign-up.
- Keychain token storage means `return` can skip sign-in.

## 7. Billing

- StoreKit 2: `Product.products(for:)`, `product.purchase()`, `Transaction.currentEntitlements`; StoreKit config files; RevenueCat.
- No StoreKit or payment code = billing measurements `not_applicable`.

## 8. Permissions

- `UNUserNotificationCenter.current().requestAuthorization(`, `CLLocationManager.request*`, `AVCaptureDevice.requestAccess`, `PHPhotoLibrary.requestAuthorization`, `CNContactStore.requestAccess`, `LAContext.evaluatePolicy` (Face ID).
- `Info.plist` `NS*UsageDescription` is the system prompt text. It counts as an explanation only if a screen shows a plain-language reason before the call.

## 9. User-facing text

- `Text("...")`, `Localizable.strings`, `Localizable.xcstrings`, `String(localized:)`.

## 10. Styles, api, jobs

### styles

- Dynamic Type: `.font(.body)` = 17pt, `.callout` 16, `.subheadline` 15, `.footnote` 13, `.caption` 12, `.caption2` 11. `.font(.system(size:))` is literal.
- Points map 1:1 to the glossary's `px`. Colors: `Color(...)`, asset catalog colors, `.foregroundStyle(.secondary)`.

### api

- Usually a separate backend. `URLSession` calls in the app are clients, not a public API.

### jobs

- Local notifications (`UNNotificationRequest`, triggers), background tasks (`BGTaskScheduler`), push handling.

## 11. First-value hints

- `first_value`: the first screen where the user saves or sees their own content.
- `upgrade`: a paywall view or limit check → `product.purchase()` → entitlement check → unlocked UI.
- `invite`: `ShareLink` or `UIActivityViewController` with an invite URL → `.onOpenURL` → shared content.
- `return`: notification or deep link → `.onOpenURL` / notification delegate → unlock or sign-in → last content.

## 12. Known traps

- Exclude: `DerivedData/`, `Pods/`, `Carthage/`, `.build/`, `*.xcassets` contents, `#Preview` blocks and `PreviewProvider` types, `*Tests/` targets.
- A view only used in previews is not a screen.
- `project.pbxproj` can be ignored except for target names.
