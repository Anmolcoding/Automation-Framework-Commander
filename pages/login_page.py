from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for login operations."""

    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    success_banner = (By.CSS_SELECTOR, ".dashboard, .welcome-message")

    def open(self):
        self.navigate("")

    def login(self, username: str, password: str):
        self.input_text(self.username_field, username)
        self.input_text(self.password_field, password)
        self.click(self.login_button)

    def is_login_successful(self) -> bool:
        return self.waits.wait_for_visible(self.success_banner) is not None
