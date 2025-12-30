import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout, poll_frequency=1)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        """Найти элемент с ожиданием"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти кликабельный элемент: {locator}")
    def find_clickable_element(self, locator):
        """Найти кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Открыть страницу: {url}")
    def go_to_url(self, url):
        """Перейти по URL"""
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url