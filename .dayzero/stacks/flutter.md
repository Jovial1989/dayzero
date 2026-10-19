# Stack guide: Flutter (flutter)

Checked: 2026-10-19. Covers Flutter 3 apps (mobile first; web and desktop targets use the same code).

## 1. Detection signals

- Strong: `lib/main.dart` containing `runApp(`.
- Weak: `pubspec.yaml` with a `flutter:` section.

## 2. Entry point

- `main()` in `lib/main.dart` → the widget passed to `runApp` → `MaterialApp`/`CupertinoApp` (`home:` or `routerConfig:`).
- The first route (`initialLocation`, `initialRoute`, or `home`) is the start of `first_value`.

## 3. Screens or commands

- Globs: `lib/**/screens/**.dart`, `lib/**/pages/**.dart`, `lib/**/views/**.dart`, `lib/**/*_screen.dart`, `lib/**/*_page.dart`.
- A screen is a widget used as a route target (`builder:`/`pageBuilder:` in a route, or pushed with `Navigator`).

## 4. Navigation

- go_router: `GoRouter(routes: [...])`, `GoRoute(path:)`, `redirect:`, `context.go(`, `context.push(`.
- Navigator 1.0: `Navigator.push(`, `pushNamed(`, `pushReplacement(`, `routes: {}`, `onGenerateRoute`.
- auto_route: `@RoutePage()`, `AutoRouter`. Deep links: `initialLocation`, platform intent filters, `uni_links`/`app_links`.

## 5. Forms and inputs

- `TextFormField` with a `validator:` that rejects empty = 1 required field. `TextField` without validation is optional.
- `Form`, `DropdownButtonFormField`, `Checkbox` required by validation.
- A swipe or tap that only moves between onboarding pages (`PageView`) counts as 1 click each.

## 6. Auth

- `firebase_auth`, `supabase_flutter`, `sign_in_with_apple`, `google_sign_in`, custom HTTP auth in a repository or service class.
- OAuth present only if a provider button calls the provider sign-in.

## 7. Billing

- `in_app_purchase` (`buyNonConsumable`, `buyConsumable`), `purchases_flutter` (RevenueCat), Stripe SDK.
- Paid flag: stored entitlement (`isPro`, `entitlements`) in `shared_preferences`, a database, or state.
- Price text in paywall widgets gives `price_visible` and `lowest_paid_usd_month`.

## 8. Permissions

- `permission_handler` (`Permission.notification.request()`, `.camera`, `.location`), `firebase_messaging.requestPermission`, `image_picker`, `geolocator`.
- Platform side: `android/app/src/main/AndroidManifest.xml` `<uses-permission>`, `ios/Runner/Info.plist` `NS*UsageDescription`.
- Explained = a visible `Text` on the same screen before the request call.

## 9. User-facing text

- `Text('...')` widgets, `lib/l10n/*.arb`, `AppLocalizations`, `intl` messages.

## 10. Styles, api, jobs

### styles

- `ThemeData`, `TextTheme` (`bodyMedium`, `bodySmall`), `lib/theme*.dart`, inline `TextStyle(fontSize:)`.
- Flutter logical pixels map 1:1 to the glossary's `px`.

### api

- Usually a separate backend. In-app: `http`, `dio` clients define what is called, not a public API. A public API exists only if the backend in the repo exposes user tokens.

### jobs

- Local notifications (`flutter_local_notifications`), FCM push, background tasks (`workmanager`). Server jobs live in the backend folder.

## 11. First-value hints

- `first_value`: the first screen where the user creates or sees their own item (first entry saved, first habit logged).
- `upgrade`: a paywall widget, a limit check (e.g. habit count), or a "Go Pro" button → purchase call → entitlement stored → confirmation screen.
- `invite`: `share_plus` with an invite link → deep link route → joined content.
- `return`: notification tap or deep link → `redirect` → sign-in if needed → last content.

## 12. Known traps

- Exclude: generated `*.g.dart`, `*.freezed.dart`, `*.gr.dart`, `*.config.dart`, `build/`, `.dart_tool/`, `ios/Pods/`, `android/.gradle/`.
- `test/` and `integration_test/` widgets are not screens.
- A route declared but never navigated to is not on the flow.
- Platform folders (`android/`, `ios/`) matter only for permissions and deep links.
