import pytest
import allure
import json

from pages.login_page import LoginPage
from utils.excel_reader import get_test_data


def _parse_test_data(raw):
    if isinstance(raw, dict):
        return raw
    try:
        return json.loads(raw)
    except Exception:
        return {}


login_test_data = get_test_data("Login")


@allure.feature("Sign In")
@pytest.mark.parametrize("data", login_test_data, ids=[d["test_case_id"] for d in login_test_data])
def test_login(driver, data):

    parsed = _parse_test_data(data)

    email = parsed.get("email", "") or ""
    password = parsed.get("password", "") or ""
    expected_result = (data.get("expected_result", "") or "").strip().lower()

    login_page = LoginPage(driver)

    with allure.step("Open landing page"):
        login_page.load()

    with allure.step("Click nav Sign In"):
        login_page.click_signin_nav()

    with allure.step(f"Enter email: {email or '(empty)'}"):
        login_page.enter_email(email)

    # Empty email: Continue button should stay disabled. Nothing further to do.
    if not email:
        with allure.step("Verify Continue is blocked for empty email"):
            assert expected_result != "success"
            assert not login_page.can_continue()
        return

    with allure.step("Click Continue"):
        login_page.click_continue()

    with allure.step("Determine next step: password field vs signup redirect"):
        branch = login_page.wait_for_next_step()

 
    if branch == "signup_redirect":
        with allure.step("Verify unrecognized email redirected to Signup"):
            assert expected_result != "success"
        return

    assert branch == "password", f"Unexpected state after Continue: {branch}"

    with allure.step(f"Enter password: {'(empty)' if not password else '****'}"):
        login_page.enter_password(password)

   
    if not password:
        with allure.step("Verify Login is blocked for empty password"):
            assert expected_result != "success"
            assert not login_page.can_login()
        return

    with allure.step("Submit login"):
        login_page.click_login()

    if expected_result == "success":
        with allure.step("Verify login success"):
            assert login_page.is_login_successful()
    else:
        with allure.step("Verify login failure"):
            assert not login_page.is_login_successful()
            assert login_page.get_error_message() is not None
