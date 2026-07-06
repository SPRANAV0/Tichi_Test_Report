from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")

    CONTINUE_BUTTON = (By.XPATH, "//button[.//text()[contains(.,'Continue')] or contains(.,'Continue')]")
    SIGNIN_BUTTON = (By.XPATH, "//button[contains(.,'Sign in') or contains(.,'Login')]")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[class*='error'], [role='alert']")
    HOME_INDICATOR = (By.CSS_SELECTOR, "[class*='dashboard'], [class*='home']")

    def load(self):
        self.open()

    def enter_email(self, email):
        self.type_text(self.EMAIL_INPUT, email)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_signin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGNIN_BUTTON)
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.click_continue()   # 🔥 important step

        if password:
            self.enter_password(password)
            self.click_signin()

    def get_error_message(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            ).text
        except:
            return None

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.HOME_INDICATOR)
            )
            return True
        except:
            return False