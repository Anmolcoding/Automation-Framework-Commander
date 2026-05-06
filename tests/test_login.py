import pytest
from pages.login_page import LoginPage
from utilities.data_reader import read_test_data
from utilities.keyword_executor import KeywordExecutor


@pytest.mark.parametrize(
    "credentials",
    read_test_data("data/login_data.json")["data_driven"],
)
def test_login_data_driven(driver, config, logger, credentials):
    login_page = LoginPage(driver, config["url"])
    logger.info(f"Executing data-driven login test: {credentials['description']}")
    login_page.open()
    login_page.login(credentials["username"], credentials["password"])
    assert login_page.is_login_successful()


def test_keyword_driven_login(driver, config, logger):
    steps = read_test_data("data/keyword_login_steps.json")
    logger.info("Executing keyword-driven login flow")
    executor = KeywordExecutor(driver)
    executor.execute(steps)
    assert KeywordExecutor(driver).waits.wait_for_visible(("css selector", ".dashboard, .welcome-message"))
