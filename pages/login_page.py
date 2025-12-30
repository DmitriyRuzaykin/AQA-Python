import allure
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_INPUT_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//input[@id='login-button']")
    WRONG_PASSWORT_LOCATOR = ("xpath", "//h3[contains(text(),'Username and password')]")
    LOCKED_USER_LOCATOR = ("xpath", "//h3[contains(text(),'locked out')]")
    EMPTY_FIELD_LOCATOR = ("xpath", "//h3[contains(text(),'Username is required')]")


    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    @allure.step("Открыть страницу логина")
    def open(self):
        """Открыть страницу логина"""
        self.go_to_url(self.url)
        return self

    @allure.step("Ввести логин: {username}")
    def enter_username(self, username):
        """Ввести имя пользователя"""
        username_field = self.find_element(self.USERNAME_INPUT_LOCATOR)
        username_field.clear()
        username_field.send_keys(username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """Ввести пароль"""
        password_field = self.find_element(self.PASSWORD_INPUT_LOCATOR)
        password_field.clear()
        password_field.send_keys(password)
        return self

    @allure.step("Нажать кнопку Login")
    def click_login(self):
        """Нажать кнопку логина"""
        login_btn = self.find_clickable_element(self.LOGIN_BUTTON_LOCATOR)
        login_btn.click()

    @allure.step("Авторизация пользователя: {username}")
    def login(self, username, pasword):
        """Цепочка действий входа"""
        self.open()
        self.enter_username(username)
        self.enter_password(pasword)
        self.click_login()
