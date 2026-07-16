from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import config


class SignupPage(BasePage):

    FIRST_NAME_INPUT = (By.CSS_SELECTOR,"input#firstName"
)

    LAST_NAME_INPUT = (By.CSS_SELECTOR,"input#lastName"
)

    EMAIL_INPUT = (By.CSS_SELECTOR,"input[type='email']"
)

    PHONE_INPUT = (By.CSS_SELECTOR,"input#phoneNumber"
)

    PASSWORD_INPUT = ( By.CSS_SELECTOR,"input#password"
)

    CONFIRM_PASSWORD_INPUT = ( By.CSS_SELECTOR,"input#confirmPassword"
)

    SIGNUP_BUTTON = (By.XPATH,"//button[normalize-space()='Sign Up']"
)

    ERROR_MESSAGE = ( By.CSS_SELECTOR,"div.text-red-500"
)

    SUCCESS_INDICATOR = (By.XPATH,"//p[normalize-space()='Home']"
)

    TERMS_CHECKBOX = (By.CSS_SELECTOR, "button[role='checkbox']#remember")

    def load(self, base_url_with_signup_path=None):
        self.open(base_url_with_signup_path or config.SIGNUP_URL)

    def signup(self, first_name, last_name, email, password, confirm_password, phone=""):
        if first_name:
            self.type_text(self.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.type_text(self.LAST_NAME_INPUT, last_name)
        if phone:
            self.type_text(self.PHONE_INPUT, phone)
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        if confirm_password:
            self.type_text(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(self.TERMS_CHECKBOX)
        self.click(self.SIGNUP_BUTTON)

    def get_error_message(self):
        if self.is_visible(self.ERROR_MESSAGE, timeout=5):
            return self.get_text(self.ERROR_MESSAGE)
        return None

    def is_signup_successful(self):
        return self.is_visible(self.SUCCESS_INDICATOR, timeout=10)
