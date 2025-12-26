from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 30, poll_frequency=1)

def test_1():
    USERNAME_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_LOCATOR = ("xpath", "//input[@id='login-button']")

    driver.get("https://www.saucedemo.com/")

    username = wait.until(EC.visibility_of_element_located(USERNAME_LOCATOR))
    password = wait.until(EC.visibility_of_element_located(PASSWORD_LOCATOR))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_LOCATOR))

    username.clear()
    password.clear()

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Тест 1 не пройден"
    print("Тест 1 успешно пройден")

def test_2():
    USERNAME_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_LOCATOR = ("xpath", "//input[@id='login-button']")

    driver.get("https://www.saucedemo.com/")

    username = wait.until(EC.visibility_of_element_located(USERNAME_LOCATOR))
    password = wait.until(EC.visibility_of_element_located(PASSWORD_LOCATOR))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_LOCATOR))

    username.clear()
    password.clear()

    username.send_keys("standard-user")
    password.send_keys("secret_sauce")
    login_button.click()

    assert driver.find_element("xpath", "//h3[text()='Epic sadface: Username and password do not match any user in this service']"), "Тест 2 не пройден"
    assert driver.current_url == "https://www.saucedemo.com/", "Текущая страница не правильная"
    print("Тест 2 успешно пройден")

def test_3():
    USERNAME_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_LOCATOR = ("xpath", "//input[@id='login-button']")

    driver.get("https://www.saucedemo.com/")

    username = wait.until(EC.visibility_of_element_located(USERNAME_LOCATOR))
    password = wait.until(EC.visibility_of_element_located(PASSWORD_LOCATOR))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_LOCATOR))

    username.clear()
    password.clear()

    username.send_keys("locked_out_user")
    password.send_keys("secret_sauce")
    login_button.click()

    assert driver.find_element("xpath", "//h3[text()='Epic sadface: Sorry, this user has been locked out.']"), "Тест 3 не пройден"
    assert driver.current_url == "https://www.saucedemo.com/", "Текущая страница не правильная"
    print("Тест 3 успешно пройден")

def test_4():
    USERNAME_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_LOCATOR = ("xpath", "//input[@id='login-button']")

    driver.get("https://www.saucedemo.com/")

    username = wait.until(EC.visibility_of_element_located(USERNAME_LOCATOR))
    password = wait.until(EC.visibility_of_element_located(PASSWORD_LOCATOR))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_LOCATOR))

    username.clear()
    password.clear()

    password.send_keys("secret_sauce")
    login_button.click()

    assert driver.find_element("xpath","//h3[text()='Epic sadface: Username is required']"), "Тест 4 не пройден"
    assert driver.current_url == "https://www.saucedemo.com/", "Текущая страница не правильная"
    print("Тест 4 успешно пройден")

def test_5():
    USERNAME_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_LOCATOR = ("xpath", "//input[@id='login-button']")

    driver.get("https://www.saucedemo.com/")

    username = wait.until(EC.visibility_of_element_located(USERNAME_LOCATOR))
    password = wait.until(EC.visibility_of_element_located(PASSWORD_LOCATOR))
    login_button = wait.until(EC.element_to_be_clickable(LOGIN_LOCATOR))

    username.clear()
    password.clear()

    username.send_keys("performance_glitch_user")
    password.send_keys("secret_sauce")
    login_button.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Тест 5 не пройден"
    print("Тест 5 успешно пройден")


test_1()
test_2()
test_3()
test_4()
test_5()