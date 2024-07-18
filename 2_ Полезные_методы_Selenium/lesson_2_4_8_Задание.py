from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from functions import calc
from functions import x_search

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 10 секунд, пока цена станет $100
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), text_="$100")
        )
    button = browser.find_element(By.ID, "book")
    button.click()
    # Решить уравнение
    x = x_search(browser)
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()

    time.sleep(10)

finally:
    time.sleep(1)
    browser.quit()