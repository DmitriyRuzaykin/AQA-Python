import allure
from pages.login_page import LoginPage


@allure.title("Успешный логин")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(driver):
    login_page = LoginPage(driver)

    with allure.step("Вводим корректные данные"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверяем успешную авторизацию"):
        assert "inventory.html" in driver.current_url

@allure.title("Неверный пароль")
@allure.severity(allure.severity_level.NORMAL)
def test_wrong_password(driver):
    login_page = LoginPage(driver)

    with allure.step("Вводим неверный пароль"):
        login_page.login("standard_user", "wrong_pass")

    with allure.step("Проверяем сообщение об ошибке"):
        error = login_page.find_element(login_page.WRONG_PASSWORT_LOCATOR)
        assert error.is_displayed()

    with allure.step("Проверяем корректность URL"):
        assert "saucedemo.com" in driver.current_url

@allure.title("Заблокированный пользователь")
@allure.severity(allure.severity_level.CRITICAL)
def test_locked_user(driver):
    login_page = LoginPage(driver)

    with allure.step("Пытаемся войти заблокированным пользователем"):
        login_page.login("locked_out_user", "secret_sauce")

    with allure.step("Проверяем сообщение о блокировке"):
        error = login_page.find_element(login_page.LOCKED_USER_LOCATOR)
        assert error.is_displayed()

    with allure.step("Проверяем корректность URL"):
        assert "saucedemo.com" in driver.current_url

@allure.title("Пустые поля")
@allure.severity(allure.severity_level.MINOR)
def test_empty_field(driver):
    login_page = LoginPage(driver)

    with allure.step("Оставляем поля пустыми"):
        login_page.login("", "")

    with allure.step("Проверяем сообщение об ошибке"):
        error = login_page.find_element(login_page.EMPTY_FIELD_LOCATOR)
        assert error.is_displayed()

    with allure.step("Проверяем корректность URL"):
        assert "saucedemo.com" in driver.current_url

@allure.title("Пользователь с задержкой")
@allure.severity(allure.severity_level.MINOR)
def test_with_a_delay(driver):
    login_page = LoginPage(driver)

    with allure.step("Логинимся пользователем с задержкой"):
        login_page.login("performance_glitch_user", "secret_sauce")

    with allure.step("Проверяем успешный вход"):
        assert "inventory.html" in driver.current_url

    with allure.step("Проверяем корректность URL"):
        assert "inventory.html" in driver.current_url