from utilities.logger import get_logger


class BaseTest:
    """Reusable base test class for common setup and helper methods."""

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.logger = get_logger("BaseTest")

    def navigate_to_base_url(self):
        self.logger.info(f"Navigating to base URL: {self.config['url']}")
        self.driver.get(self.config["url"])

    def take_screenshot(self, name: str):
        self.logger.info(f"Capturing screenshot: {name}")
        self.driver.save_screenshot(f"reports/{name}.png")
