import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


@pytest.fixture
def start():
    # Настройка опций
    capabilities = config.capabilities

    driver = webdriver.Remote(command_executor=config.WEBDRIVER_URL,
                              desired_capabilities=capabilities)
    # Переход на страницу
    driver.get(config.DRIVER_URL)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "accept-choices"))
        )
        driver.find_element(By.ID, "accept-choices").click()
    except AssertionError as e:
        print("Ошибка:", e)

    yield driver
    driver.quit()

    return driver
