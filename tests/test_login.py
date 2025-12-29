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

        current_url = driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"

        if current_url == expected_url:
            print("✅ ТЕСТ 1 ПРОЙДЕН! Пользователь успешно авторизован.")
            return True
        else:
            print("❌ ТЕСТ 1 НЕ ПРОЙДЕН! Неверный URL после логина.")
            return False

    except Exception as e:
        print(f"🔥 КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        if driver:
            print("🧹 Закрываю браузер...")
            driver.quit()

def test_2():
    driver = None

    try:
        driver = setup_driver()
        login_page = LoginPage(driver)

        print("🌐 Открываю страницу логина...")

        login_page.login("standard-user", "secret_sauce")

        ERROR_MESSAGE_LOCATOR = ("xpath", "//h3[text()='Epic sadface: Username and password do not match any user in this service']")
        error_message = login_page.find_element(ERROR_MESSAGE_LOCATOR)

        current_url = driver.current_url
        expected_url = "https://www.saucedemo.com/"

        if (current_url == expected_url and error_message.is_displayed()):
            print("✅ ТЕСТ 2 ПРОЙДЕН! Пользователь не авторизован с неверным логином.")
            return True
        else:
            print("❌ ТЕСТ 2 НЕ ПРОЙДЕН!")
            return False

    except Exception as e:
        print(f"🔥 КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        if driver:
            print("🧹 Закрываю браузер...")
            driver.quit()


if __name__ == "__main__":
    test_1()
    print("------------")
    test_2()