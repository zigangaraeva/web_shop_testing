import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from page_objects.login_page import LoginPage


load_dotenv()

@pytest.fixture
def browser(request):
    service = Service('C:/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    def quit_browser():
        driver.quit()

    request.addfinalizer(quit_browser)
    return driver

@pytest.fixture
def authorized_browser(browser):
    login = LoginPage(browser)
    login.open("https://demowebshop.tricentis.com/login")
    login.enter_login("alina.zigangaraeva@gmail.com")
    login.enter_password("zvsQfyrP3DG!Y9")
    login.click_login_button()
    login.welcome_page()
    return browser
