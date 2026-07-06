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

    email = parsed.get("email", "")
    password = parsed.get("password", "")
    expected_result = data.get("expected_result", "")

    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.load()

    with allure.step(f"Enter email: {email}"):
        login_page.enter_email(email)

    with allure.step("Click Continue"):
        login_page.click_continue()

    # 👉 If your app has 2-step login (email → password)
    if password:
        with allure.step("Enter password"):
            login_page.enter_password(password)

        with allure.step("Submit login"):
            login_page.submit_login()

    if expected_result.lower() == "success":
        with allure.step("Verify login success"):
            assert login_page.is_login_successful()
    else:
        with allure.step("Verify login failure"):
            assert not login_page.is_login_successful()
            assert login_page.get_error_message() is not None