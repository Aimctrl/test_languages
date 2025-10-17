import time
from selenium.webdriver.common.by import By

def test_localization_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)

    assert browser.find_element(By.CSS_SELECTOR, '[class*="btn-add-to-basket"]')
