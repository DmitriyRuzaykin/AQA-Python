from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


def setup_driver():
    """Настройка и создание драйвера"""
    print("🔄 Настраиваю Chrome драйвер...")

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

def test_1():
    driver = None

    try:
        driver = setup_driver()
        login_page = LoginPage(driver)

        print("🌐 Открываю страницу логина...")

        login_page.login("standard_user", "secret_sauce")

        assert "saucedemo.com/inventory.html" in driver.current_url

        print("✅ ТЕСТ 1 ПРОЙДЕН! Пользователь авторизован.")

    except Exception as e:
        print(f"🔥 КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()

def test_2():
    driver = None

    try:
        driver = setup_driver()
        login_page = LoginPage(driver)

        print("🌐 Открываю страницу логина...")

        login_page.login("standard_user", "secret-sauce")

        ERROR_MESSAGE_LOCATOR = ("xpath",
                                 "//h3[text()='Epic sadface: Username and password do not match any user in this service']")
        error_message = login_page.find_element(ERROR_MESSAGE_LOCATOR)

        assert error_message.is_displayed()
        assert "saucedemo.com" in driver.current_url

        print("✅ ТЕСТ 2 ПРОЙДЕН! Пользователь не авторизован.")

    except Exception as e:
        print(f"🔥 КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()

def test_3():
    driver = None

    try:
        driver = setup_driver()
        login_page = LoginPage(driver)

        print("🌐 Открываю страницу логина...")

        login_page.login("locked_out_user", "secret_sauce")

        ERROR_MESSAGE_LOCATOR = ("xpath",
                                 "//h3[text()='Epic sadface: Sorry, this user has been locked out.']")
        error_message = login_page.find_element(ERROR_MESSAGE_LOCATOR)

        assert error_message.is_displayed()
        assert "saucedemo.com" in driver.current_url

        print("✅ ТЕСТ 3 ПРОЙДЕН! Пользователь заблокирован.")

    except Exception as e:
        print(f"🔥 КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()

    finally:
        if driver:
            print("🧹 Закрываю браузер...")
            driver.quit()

def test_4():
    driver = None

    try:
        driver = setup_driver()
        login_page = LoginPage(driver)

        print("🌐 Открываю страницу логина...")

        login_page.login("", "")

        ERROR_MESSAGE_LOCATOR = ("xpath",
                                     "//h3[text()='Epic sadface: Username is required']")
        error_message = login_page.find_element(ERROR_MESSAGE_LOCATOR)

        assert error_message.is_displayed()
        assert "saucedemo.com" in driver.current_url

        print("✅ ТЕСТ 4 ПРОЙДЕН! Пользователь не авторизован.")

    except Exception as e:
        print(f"🔥 КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()

    finally:
        if driver:
            print("🧹 Закрываю браузер...")
            driver.quit()

if __name__ == "__main__":

    test_1()
    print("------------")
    test_2()
    print("------------")
    test_3()
    print("------------")
    test_4()
