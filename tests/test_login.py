import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    print("\n🔄 Запуск Chrome")

    options = Options()
    options.add_argument("--incognito")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    print("\n🧹 Закрытие браузера")
    driver.quit()

def test_1():
    def test_login_success(driver):
        login_page = LoginPage(driver)

        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in driver.current_url

def test_2():
    login_page = LoginPage(driver)

    login_page.login("standard_user", "wrong_password")

    error = login_page.find_element(
        ("xpath", "//h3[contains(text(),'Username and password')]")
    )

    assert error.is_displayed()

def test_3():
    login_page = LoginPage(driver)

    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.find_element(
        ("xpath", "//h3[contains(text(),'locked out')]")
    )

    assert error.is_displayed()

def test_4():
    login_page = LoginPage(driver)

    login_page.login("", "")

    error = login_page.find_element(
        ("xpath", "//h3[contains(text(),'Username is required')]")
    )

    assert error.is_displayed()

def test_5():
    login_page = LoginPage(driver)

    login_page.login("performance_glitch_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

if __name__ == "__main__":

    test_1()
    print("------------")
    test_2()
    print("------------")
    test_3()
    print("------------")
    test_4()
    print("------------")
    test_5()