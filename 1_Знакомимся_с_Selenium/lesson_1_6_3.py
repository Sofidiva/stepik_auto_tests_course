from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

try:
    fake = Faker()
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    #elements = browser.find_elements(By.TAG_NAME, "input")
    #elements = browser.find_elements(By.XPATH, "//*[@type='text']")
    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for element in elements:
        word = fake.word()
        element.send_keys(word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()