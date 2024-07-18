import math
from selenium.webdriver.common.by import By


def x_search(browser):
    return browser.find_element(By.CSS_SELECTOR, "#input_value").text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
