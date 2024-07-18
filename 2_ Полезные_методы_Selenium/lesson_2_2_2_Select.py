from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)
    '''# 1-й вариант
    browser.find_element(By.TAG_NAME, "select").click()

    #browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    # ИЛИ
    browser.find_element(By.CSS_SELECTOR, "[value='1']").click()'''

    # 2-й вариант
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_value("1")                             # ищем элемент с текстом "1"
    #select.select_by_visible_text("34")                   # select.select_by_visible_text("text") ищем элемент с текстом "34"
    select.select_by_index(1)                               # select.select_by_index(index) ищем элемент с индексом 1


    time.sleep(3)
finally:
    time.sleep(3)
    browser.quit()