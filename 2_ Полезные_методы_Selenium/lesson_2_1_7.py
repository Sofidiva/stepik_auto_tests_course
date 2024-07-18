from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    treasure_element = browser.find_element(By.CSS_SELECTOR, "#treasure")

    x = treasure_element.get_attribute("valuex")
    y = calc(x)

    print(x)
    print(type(x))

    # Заполняем поле значением x
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    time.sleep(1)

    # Нажимаем на чек-бокс I'm the robot
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()

    # Нажимаем на радиобаттон "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()

    time.sleep(1)

    # Нажимаем на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()