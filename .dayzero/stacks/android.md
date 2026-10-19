# Stack guide: Native Android (android)

Checked: 2026-10-19. Covers Kotlin or Java apps with Jetpack Compose or XML views.

## 1. Detection signals

- Strong: `AndroidManifest.xml` with an `<activity>` and a Kotlin/Java class extending `Activity`, `ComponentActivity`, `AppCompatActivity` or `FragmentActivity`.
- Weak: `build.gradle(.kts)` applying `com.android.application`.
- Kotlin or Compose Multiplatform: trace the Android side only and say so.

## 2. Entry point

- The activity with the `MAIN` / `LAUNCHER` intent filter in `AndroidManifest.xml` → `setContent { }` (Compose) or `setContentView(` (XML).
- A splash or launch activity that immediately routes elsewhere is not the first screen; follow it.

## 3. Screens or commands

- Compose: `@Composable` functions used as `composable("route") { }` destinations; globs `**/ui/**/*Screen.kt`, `**/screens/**`.
- XML: Activities and Fragments with layouts in `res/layout/*.xml`.

## 4. Navigation

- Compose: `NavHost(`, `composable(`, `navController.navigate(`, `popUpTo`, start destination.
- XML: `res/navigation/*.xml` nav graphs, `findNavController().navigate(`, `startActivity(Intent(`.
- Deep links: `<intent-filter>` with `<data android:scheme>`, `navDeepLink { }`.

## 5. Forms and inputs

- Compose `TextField` / `OutlinedTextField` with validation that blocks submit; XML `EditText` with `setError`.
- Password + confirm = 2 fields.

## 6. Auth

- Credential Manager (`GetGoogleIdOption`, `GetSignInWithGoogleOption` = OAuth), Firebase Auth, Google Sign-In, custom API login.
- Session in DataStore or EncryptedSharedPreferences lets `return` skip `signin`.

## 7. Billing

- Play Billing: `BillingClient`, `launchBillingFlow(`, `acknowledgePurchase(`, `queryPurchasesAsync(`; RevenueCat Android.
- Paid flag: acknowledged purchase stored (DataStore, Room, server) or entitlement check.

## 8. Permissions

- Declared in `AndroidManifest.xml` `<uses-permission>`. Requested with `rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission())`, `registerForActivityResult`, or `ActivityCompat.requestPermissions(`.
- Normal permissions (INTERNET) are not prompts. Runtime prompts: POST_NOTIFICATIONS, CAMERA, ACCESS_*_LOCATION, READ_CONTACTS, RECORD_AUDIO, READ_MEDIA_*.
- Explained = a visible text on the same screen before the launcher call. A tap on the OS dialog counts 1.

## 9. User-facing text

- `res/values/strings.xml` (and `values-xx/`), `stringResource(R.string.)`, literal `Text("...")`.

## 10. Styles, api, jobs

### styles

- Compose `Typography` in `ui/theme/Type.kt`, inline `fontSize = 14.sp`; XML `android:textSize`, `res/values/themes.xml`, `colors.xml`.
- `sp` and `dp` map 1:1 to the glossary's `px`.

### api

- Retrofit/Ktor clients in the app are not a public API.

### jobs

- WorkManager (`PeriodicWorkRequest`), `AlarmManager`, Firebase Messaging service, notification channels.

## 11. First-value hints

- `first_value`: the first screen where the user saves or sees their own item.
- `upgrade`: paywall composable or limit check → `launchBillingFlow` → acknowledged purchase → unlocked screen.
- `invite`: `Intent.ACTION_SEND` with a link → deep link intent filter → shared content.
- `return`: notification `PendingIntent` or deep link → session check → last content.

## 12. Known traps

- Exclude: `build/`, `.gradle/`, `app/build/`, generated `R` and `BuildConfig`, `**/test/**`, `**/androidTest/**`.
- `@Preview` composables are not screens.
- A manifest missing the launcher activity or `android:name` is a dead end at step 1: report it, do not skip it.
