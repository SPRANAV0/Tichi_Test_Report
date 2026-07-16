from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    # Landing page
    NAV_SIGNIN_BUTTON = (By.XPATH, "//nav//button[normalize-space()='Sign In']")

    # Step 1: email
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#email")
    CONTINUE_BUTTON = (By.XPATH, "//button[@type='submit'][normalize-space()='Continue']")

    # Step 2a: password (existing/recognized email)
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit'][normalize-space()='Login']")

    # Step 2b: unrecognized email -> app auto-redirects to Signup instead
    SIGNUP_REDIRECT_INDICATOR = (By.CSS_SELECTOR, "input#firstName")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.text-red-500.text-center.text-sm.mb-2")
    HOME_INDICATOR = (By.XPATH, "//p[normalize-space()='Home']")

    def load(self):
        self.open()

    def click_signin_nav(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NAV_SIGNIN_BUTTON)
        ).click()

    def enter_email(self, email):
        self.type_text(self.EMAIL_INPUT, email)

    def can_continue(self, timeout=3):
        """Returns False if the Continue button is disabled/unclickable (e.g. empty email)."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.CONTINUE_BUTTON)
            )
            return True
        except Exception:
            return False

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def wait_for_next_step(self, timeout=10):
        """
        After clicking Continue, the app either shows a password field
        (recognized email) or redirects into the Signup form (unrecognized
        email). Returns "password", "signup_redirect", or "timeout".
        """
        self._wait_either(timeout)
        if self.is_visible(self.SIGNUP_REDIRECT_INDICATOR, timeout=1):
            return "signup_redirect"
        if self.is_visible(self.PASSWORD_INPUT, timeout=1):
            return "password"
        return "timeout"

    def _wait_either(self, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self.is_visible(self.PASSWORD_INPUT, timeout=1)
                or self.is_visible(self.SIGNUP_REDIRECT_INDICATOR, timeout=1)
            )
            return True
        except Exception:
            return False

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def can_login(self, timeout=3):
        """Returns False if the Login button is disabled/unclickable (e.g. empty password)."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.LOGIN_BUTTON)
            )
            return True
        except Exception:
            return False

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_error_message(self):
        if self.is_visible(self.ERROR_MESSAGE, timeout=5):
            return self.get_text(self.ERROR_MESSAGE)
        return None

    def is_login_successful(self):
        return self.is_visible(self.HOME_INDICATOR, timeout=10)
