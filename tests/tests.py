from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

USERNAME_LOCATOR = ("xpath", "//input[@id='user-name']")
PASSWORD_LOCATOR = ("xpath", "//input[@id='password']")
LOGIN_LOCATOR = ("xpath", "//input[@id='login-button']")

driver.get("https://www.saucedemo.com/")

username = wait.until(EC.visibility_of_element_located(USERNAME_LOCATOR))
password = wait.until(EC.visibility_of_element_located(PASSWORD_LOCATOR))
login_button = wait.until(EC.element_to_be_clickable(LOGIN_LOCATOR))

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()