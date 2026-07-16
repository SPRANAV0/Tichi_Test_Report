# Tichi Web App — Sign In / Sign Up Automation (Pytest + Selenium + Allure)

A simple UI automation project for the Sign In and Sign Up flows of:
https://tichi-app-webapp-stage.web.app

## Project structure

```
tichi_automation/
├── config/
│   └── config.py          # Base URL, timeouts, browser settings
├── data/
│   └── test_data.xlsx      # Excel test data (Login & Signup sheets)
├── pages/
│   ├── base_page.py         # Common Selenium helper methods
│   ├── login_page.py        # Login page locators/actions
│   └── signup_page.py       # Signup page locators/actions
├── tests/
│   ├── test_signin.py       # Data-driven login tests
│   └── test_signup.py       # Data-driven signup tests
├── conftest.py              # WebDriver fixture + screenshot-on-failure
├── pytest.ini
├── requirements.txt
└── reports/                 # Allure results/report generated here
```

## 1. Setup

Requires Python 3.9+, Google Chrome installed, and internet access.

```bash
cd tichi_automation
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Allure also needs its command-line tool (separate from `allure-pytest`) to
generate/view the HTML report:

- **Mac:** `brew install allure`
- **Windows:** `scoop install allure`
- **Linux:** download from https://github.com/allure-framework/allure2/releases,
  unzip, and add the `bin` folder to your PATH.

## 2. Test data

Test data lives in `data/test_data.xlsx`:

- **Login** sheet: `test_case_id | email | password | expected_result`
- **Signup** sheet: `test_case_id | name | email | password | confirm_password | expected_result`

The valid login credentials you gave me are already in row `TC_LOGIN_01`:
`spranavsivaraj@gmail.com` / `Pranav@19` → `expected_result = success`.

Add/edit rows directly in Excel — the tests will pick up any row you add automatically.

## 3. Fixed in this version

The following bugs from the initial draft have been corrected so the suite
runs cleanly end-to-end (no `AttributeError`/`TypeError`):

- `tests/test_signin.py` called a non-existent `login_page.submit_login()` —
  now calls the actual `click_signin()` method.
- `tests/test_signup.py` called `signup_page.load()` with no URL, but
  `SignupPage.load()` required one — `config.SIGNUP_URL` was added and
  `load()` now defaults to it.
- `tests/test_signup.py` called `signup_page.signup(name, email, password)`
  with 3 args while the method requires 4 (`confirm_password`) — now passes
  `confirm_password` from the Excel row.
- Added null-guards around `expected_result.lower()` and other Excel cells
  so a blank cell won't raise `AttributeError: 'NoneType' object has no
  attribute 'lower'`.
- Replaced bare `except:` clauses with `except Exception:`.
- Removed the bundled Windows `venv/` and stale `__pycache__` /
  `allure-results` / `reports` folders from the zip — create your own venv
  per step 1 instead of reusing the shipped one.

## 4. IMPORTANT — verify locators before running

I could not inspect the live rendered DOM of the app from this environment
(it's a client-rendered SPA, so a plain HTTP fetch only returns an empty shell).
The locators in `pages/login_page.py` and `pages/signup_page.py` are
best-effort guesses based on common patterns (input types, placeholder text,
button text like "Sign in" / "Sign up").

Before running the suite:
1. Open the app in Chrome.
2. Press `F12` → use the element picker on the email field, password field,
   and the sign-in/sign-up buttons.
3. Update the `By.CSS_SELECTOR` / `By.XPATH` values in the two page objects
   to match what you see.
4. Also confirm the actual signup route (I assumed `/signup` in
   `tests/test_signup.py` — change `SIGNUP_URL` if it's different, e.g. a
   modal on the same page instead of a separate route).

## 5. Run the tests

```bash
pytest
```

This runs everything under `tests/` and writes raw Allure results to
`reports/allure-results/` (configured in `pytest.ini`).

Run only login or only signup tests:

```bash
pytest tests/test_signin.py
pytest tests/test_signup.py
```

Run a single Excel-driven case by its test id:

```bash
pytest tests/test_signin.py -k TC_LOGIN_01
```

## 6. Generate & view the Allure report

```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

This opens an interactive HTML report with a pass/fail summary, per-test
steps (from the `allure.step()` calls in the tests), and screenshots
automatically attached to any failing test.

## Notes / assumptions

- Selenium + Chrome is used (via `webdriver-manager`, so no manual chromedriver
  download needed).
- Tests are data-driven off the Excel file using `pytest.mark.parametrize`,
  so each row becomes its own test case in the report.
- `HEADLESS = False` in `config/config.py` by default so you can watch it run;
  set to `True` for CI.
- This is intentionally a minimal starting framework (per your request for
  "very basic and simple") — no retry logic, parallelization, or CI config
  included, but the structure is set up so you can add those later without
  restructuring.
