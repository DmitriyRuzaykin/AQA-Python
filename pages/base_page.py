from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout, pool_frequency=1)

    def find_element(self, locator):
        """Найти элемент с ожиданием"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator):
        """Найти кликабельный элемент"""
        return self.wait.until(EC.element_to_be_clickable(self, locator))

    def go_to_url(self, url):
        """Перейти по URL"""
        self.driver.get(url)

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url