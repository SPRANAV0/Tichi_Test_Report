from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignupPage(BasePage):

    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name'], input[placeholder*='name' i]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'], input[name='email'], input[placeholder*='mail' i]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'][name='password'], input[name='password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='confirmPassword'], input[placeholder*='confirm' i]")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(translate(., 'SIGNUP', 'signup'), 'sign up') or contains(translate(., 'SIGNUP', 'signup'), 'register') or contains(translate(., 'SIGNUP', 'signup'), 'create account')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[class*='error'], [role='alert']")
    SUCCESS_INDICATOR = (By.CSS_SELECTOR, "[class*='dashboard'], [class*='home'], [class*='verify']")

    def load(self, base_url_with_signup_path):
        self.open(base_url_with_signup_path)

    def signup(self, name, email, password, confirm_password):
        if name:
            self.type_text(self.NAME_INPUT, name)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        if confirm_password:
            self.type_text(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(self.SIGNUP_BUTTON)

    def get_error_message(self):
        if self.is_visible(self.ERROR_MESSAGE, timeout=5):
            return self.get_text(self.ERROR_MESSAGE)
        return None

    def is_signup_successful(self):
        return self.is_visible(self.SUCCESS_INDICATOR, timeout=10)
