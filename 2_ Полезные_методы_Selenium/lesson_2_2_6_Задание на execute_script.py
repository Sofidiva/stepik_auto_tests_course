from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Считать значение для переменной x.
    # Посчитать математическую функцию от x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # Ввести ответ в текстовое поле.
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    # Проскроллить страницу вниз
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Нажимаем на чек-бокс I'm the robot
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    # Нажимаем на радиобаттон "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()
    # Нажать на кнопку "Submit".
    button.click()

    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()

