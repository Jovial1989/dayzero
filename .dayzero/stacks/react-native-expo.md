# Stack guide: React Native and Expo (react-native-expo)

Checked: 2026-10-19. Covers Expo (managed, expo-router or React Navigation) and bare React Native.

## 1. Detection signals

- Strong: `package.json` dependency `expo` or `react-native`; `app.json` / `app.config.(js|ts)` with an `expo` key; `index.js` calling `AppRegistry.registerComponent(`.
- Weak: `android/` and `ios/` folders next to a `package.json`.
- Beats `nextjs-react`: both list `react`, but `react-native`/`expo` decides. Bare React Native (no `expo`) uses this guide, noted as bare.

## 2. Entry point

- expo-router: `app/_layout.tsx` is the root; `app/index.tsx` is the first screen.
- React Navigation: `App.tsx` → `NavigationContainer` → the first screen of the root navigator (`initialRouteName` or the first `<Stack.Screen>`).

## 3. Screens or commands

- Globs: `app/**/*.tsx` (expo-router, excluding `_layout.tsx` and `+not-found.tsx`), `src/screens/**`, `screens/**`, `**/*Screen.tsx`.
- Route groups `(tabs)` and dynamic segments `[id]` are URL rules, not separate screens.

## 4. Navigation

- expo-router: `<Link href>`, `router.push(`, `router.replace(`, `<Redirect href>`, `Stack`, `Tabs`, `useSegments` guards in `_layout.tsx`.
- React Navigation: `createNativeStackNavigator`, `createBottomTabNavigator`, `navigation.navigate(`, `navigation.reset(`.
- Deep links: `scheme` in `app.json`, `Linking`, notification response handlers that navigate.

## 5. Forms and inputs

- `TextInput` with required checks, react-hook-form (`rules: { required }`), Formik + Yup/Zod.
- Password + confirm = 2 fields. Pickers and switches count only when validation requires them.

## 6. Auth

- expo-auth-session (Google, Apple, GitHub providers = OAuth), `expo-apple-authentication`, Clerk Expo, Supabase, Firebase Auth.
- Session in `expo-secure-store` or AsyncStorage lets `return` skip `signin`.

## 7. Billing

- `react-native-purchases` (RevenueCat: `Purchases.purchasePackage(`, `customerInfo.entitlements`), `expo-iap` / `react-native-iap`, Stripe React Native.
- Paid flag: an entitlement check or a stored `isPro`. A paywall screen alone is `upgrade_offer`, not `paid_active`.

## 8. Permissions

- `expo-notifications` (`requestPermissionsAsync`), `expo-location`, `expo-camera`, `expo-image-picker`, `expo-contacts`, `expo-media-library`.
- Declared in `app.json` (`android.permissions`, `ios.infoPlist` usage strings). Explained = a visible `Text` on the same screen before the request call.
- A tap on the OS permission dialog counts as 1 click.

## 9. User-facing text

- JSX `<Text>` content, `i18n-js`, i18next resources, `locales/*.json`, `app.json` `name`.

## 10. Styles, api, jobs

### styles

- `StyleSheet.create`, inline `style={{ fontSize }}`, theme files (`src/theme.ts`), NativeWind classes (`text-xs` 12, `text-sm` 14, `text-base` 16).
- React Native density-independent units map 1:1 to the glossary's `px`.

### api

- Usually a separate backend. `fetch`/axios clients in the app are not a public API.

### jobs

- `expo-notifications` scheduling, `expo-background-fetch`, `expo-task-manager`, push token registration.

## 11. First-value hints

- `first_value`: the first screen where the user saves or sees their own item.
- `upgrade`: paywall screen or limit check → purchase call → entitlement active → confirmation.
- `invite`: `Share.share` / `expo-sharing` with an invite link → deep link route → shared content.
- `return`: notification tap or deep link → auth guard in `_layout.tsx` → last content.

## 12. Known traps

- Exclude: `node_modules/`, `.expo/`, `android/app/build/`, `ios/Pods/`, `ios/build/`, `*.generated.*`, `__tests__/`.
- `app/_layout.tsx` is a layout, not a screen. `+html.tsx` is web-only.
- A web build (`react-native-web`) does not make it `nextjs-react`.
