from pages.base_page import BasePage

class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = ("xpath", "//input[@id='user-name']")
    PASSWORD_INPUT = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//input[@id='login-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def open(self):
        """Открыть страницу логина"""
        self.go_to_url(self.url)
        return self

    def enter_username(self, username):
        """Ввести имя пользователя"""
        username_field = self.find_element(self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)
        return self

    def enter_password(self, password):
        """Ввести пароль"""
        password_field = self.find_element(self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login(self):
        """Нажать кнопку логина"""
        login_btn = self.find_clickable_element(self.LOGIN_BUTTON)
        login_btn.click()

    def login(self, username, pasword):
        """Цепочка действий входа"""
        self.open()
        self.enter_username(username)
        self.enter_password(pasword)
        self.click_login()
