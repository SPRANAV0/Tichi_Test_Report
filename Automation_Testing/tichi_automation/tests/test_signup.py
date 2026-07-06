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
    except:
        return {}


signup_test_data = get_test_data("Signup")


@allure.feature("Sign Up")
@pytest.mark.parametrize("data", signup_test_data, ids=[d["test_case_id"] for d in signup_test_data])
def test_signup(driver, data):

    parsed = _parse_test_data(data)

    name = parsed.get("name", "")
    email = parsed.get("email", "")
    password = parsed.get("password", "")
    expected_result = data.get("expected_result", "")

    signup_page = SignupPage(driver)

    with allure.step("Open signup page"):
        signup_page.load()

    with allure.step("Fill signup form"):
        signup_page.signup(name, email, password)

    if expected_result.lower() == "success":
        with allure.step("Verify signup success"):
            assert signup_page.is_signup_successful()
    else:
        with allure.step("Verify signup failure"):
            assert not signup_page.is_signup_successful()
            assert signup_page.get_error_message() is not None