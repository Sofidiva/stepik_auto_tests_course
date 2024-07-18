import time
from selenium import webdriver
from selenium.webdriver.common.by import By

''' # 2.2.4
browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
browser.execute_script("document.title='Script executing';alert('Robots at work');")
'''
# 2.2.5 Пример задачи для execute_script.
# Клик на перекрытый элемент
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.
# Эта команда проскроллит страницу на 100 пикселей вниз:
browser.execute_script("window.scrollBy(0, 100);")

# // javascript. Для сравнения скрипт на языке javascript, который делает то же, что приведенный выше пример для WebDriver:
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);


time.sleep(10)