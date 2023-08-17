import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
from enums.selectors import Main_Selectors


@pytest.fixture
def start():
    # Настройка опций
    capabilities = config.capabilities

    driver = webdriver.Remote(command_executor=config.webdriver_url,
                              desired_capabilities=capabilities)
    # Переход на страницу
    driver.get(config.driver_url)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, Main_Selectors.POLICY_POPUP_ACCEPT_BUTTON.value))
        )
        driver.find_element(By.ID, Main_Selectors.POLICY_POPUP_ACCEPT_BUTTON.value).click()
    except AssertionError as e:
        print("Ошибка:", e)

    yield driver
    driver.quit()

    return driver
