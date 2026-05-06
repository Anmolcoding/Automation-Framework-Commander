import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    """Factory that creates browser driver instances based on configuration."""

    def __init__(self, config: dict):
        self.config = config
        self.browser = config.get("browser", "chrome").lower()
        self.headless = config.get("headless", False)
        self.implicit_wait = config.get("implicit_wait", 10)
        self.page_load_timeout = config.get("page_load_timeout", 30)

    def create_driver(self):
        if self.browser == "chrome":
            return self._create_chrome()
        if self.browser == "firefox":
            return self._create_firefox()
        if self.browser == "edge":
            return self._create_edge()
        raise ValueError(f"Unsupported browser: {self.browser}")

    def _common_setup(self, driver):
        driver.implicitly_wait(self.implicit_wait)
        driver.set_page_load_timeout(self.page_load_timeout)
        return driver

    def _create_chrome(self):
        options = ChromeOptions()
        if self.headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        service = ChromeService(ChromeDriverManager().install())
        return self._common_setup(webdriver.Chrome(service=service, options=options))

    def _create_firefox(self):
        options = FirefoxOptions()
        if self.headless:
            options.add_argument("-headless")
        service = FirefoxService(GeckoDriverManager().install())
        return self._common_setup(webdriver.Firefox(service=service, options=options))

    def _create_edge(self):
        options = EdgeOptions()
        if self.headless:
            options.add_argument("--headless=new")
        service = EdgeService(EdgeChromiumDriverManager().install())
        return self._common_setup(webdriver.Edge(service=service, options=options))
