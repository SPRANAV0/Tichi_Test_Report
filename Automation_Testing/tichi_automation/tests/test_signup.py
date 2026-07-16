import pytest
import allure
from pages.signup_page import SignupPage
from utils.excel_reader import get_test_data
import json


def _parse_test_data(raw):
    if isinstance(raw, dict):
        return raw
    try:
        return json.loads(raw)
    except Exception:
        return {}


signup_test_data = get_test_data("Signup")


@allure.feature("Sign Up")
@pytest.mark.parametrize("data", signup_test_data, ids=[d["test_case_id"] for d in signup_test_data])
def test_signup(driver, data):

    parsed = _parse_test_data(data)

    name = parsed.get("name", "") or ""
    name_parts = name.split(" ", 1)
    first_name = name_parts[0] if name_parts else ""
    last_name = name_parts[1] if len(name_parts) > 1 else ""
    email = parsed.get("email", "") or ""
    password = parsed.get("password", "") or ""
    confirm_password = parsed.get("confirm_password", "") or ""
    phone = parsed.get("phone", "") or ""
    expected_result = (data.get("expected_result", "") or "").strip()

    signup_page = SignupPage(driver)

    with allure.step("Open signup page"):
        signup_page.load()

    with allure.step("Fill signup form"):
        signup_page.signup(first_name, last_name, email, password, confirm_password, phone)

    if expected_result.lower() == "success":
        with allure.step("Verify signup success"):
            assert signup_page.is_signup_successful()
    else:
        with allure.step("Verify signup failure"):
            assert not signup_page.is_signup_successful()
            assert signup_page.get_error_message() is not None