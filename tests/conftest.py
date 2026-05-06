import pytest
from utilities.config_reader import ConfigReader
from utilities.driver_factory import DriverFactory
from utilities.logger import get_logger


@pytest.fixture(scope="session")
def config():
    reader = ConfigReader()
    return reader.get_environment_config()


@pytest.fixture(scope="session")
def logger():
    return get_logger("automation_framework")


@pytest.fixture(scope="function")
def driver(config, logger):
    factory = DriverFactory(config)
    driver_instance = factory.create_driver()
    logger.info(f"Starting browser session for {config['browser']} on {config['environment']}")
    driver_instance.maximize_window()
    yield driver_instance
    logger.info("Closing browser session")
    driver_instance.quit()
