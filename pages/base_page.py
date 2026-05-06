from selenium.webdriver.remote.webdriver import WebDriver
from utilities.wait_utils import WaitUtils


class BasePage:
    """Base page object with common actions and helpers."""

    def __init__(self, driver: WebDriver, base_url: str = None):
        self.driver = driver
        self.base_url = base_url
        self.waits = WaitUtils(driver)

    def navigate(self, path: str = ""):
        if not self.base_url:
            raise ValueError("Base URL is not configured for this page.")
        self.driver.get(self.base_url.rstrip("/") + "/" + path.lstrip("/"))

    def click(self, locator):
        self.waits.wait_for_clickable(locator).click()

    def input_text(self, locator, text: str):
        field = self.waits.wait_for_visible(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator) -> str:
        return self.waits.wait_for_visible(locator).text
