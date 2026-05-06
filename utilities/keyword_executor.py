import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utilities.wait_utils import WaitUtils


BY_MAP = {
    "id": By.ID,
    "name": By.NAME,
    "css": By.CSS_SELECTOR,
    "css selector": By.CSS_SELECTOR,
    "xpath": By.XPATH,
    "class_name": By.CLASS_NAME,
    "link_text": By.LINK_TEXT,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
    "tag_name": By.TAG_NAME,
}


def parse_locator(locator: dict):
    locator_type = locator.get("by", "css").lower()
    locator_value = locator.get("value")
    if locator_type not in BY_MAP:
        raise ValueError(f"Unsupported locator type: {locator_type}")
    return BY_MAP[locator_type], locator_value


class KeywordExecutor:
    """Simple keyword engine for hybrid automation workflows."""

    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.waits = WaitUtils(driver, timeout=timeout)
        self.logger = logging.getLogger("KeywordExecutor")

    def execute(self, steps: list):
        for step in steps:
            action = step.get("action")
            locator = step.get("locator")
            value = step.get("value")

            if action == "open_url":
                self.logger.info(f"Opening URL: {value}")
                self.driver.get(value)
                continue

            if locator is None:
                raise ValueError(f"Locator is required for action: {action}")

            parsed_locator = parse_locator(locator)
            if action == "input_text":
                element = self.waits.wait_for_visible(parsed_locator)
                element.clear()
                element.send_keys(value)
                continue

            if action == "click":
                element = self.waits.wait_for_clickable(parsed_locator)
                element.click()
                continue

            if action == "assert_text":
                self.waits.wait_for_text(parsed_locator, value)
                continue

            raise ValueError(f"Unsupported keyword action: {action}")
