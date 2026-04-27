from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    WebDriverWait(driver, 10).until(
    EC.url_contains("inventory")
    )

    assert "inventory" in driver.current_url

    #driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    login = LoginPage(driver)
    login.enter_username("wrong_user")
    login.enter_password("wrong_pass")
    login.click_login()

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
    )

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text

    assert "Epic sadface" in error_message

    #driver.quit()
