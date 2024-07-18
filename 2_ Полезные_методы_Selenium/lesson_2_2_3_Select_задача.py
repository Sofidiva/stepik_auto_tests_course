from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)
    # 1-й вариант
    # найти параметр x
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    print(x)
    # найти параметр y
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    print(y)
    # Найти сумму
    sum_elements = str(int(x) + int(y))
    print(sum_elements)
    # открыть выпадающий список
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    # клик на элемент
    select.select_by_value(sum_elements)                               # ищем элемент с текстом
    # Нажать кнопку Submit
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    time.sleep(2)
finally:
    time.sleep(10)
    browser.quit()