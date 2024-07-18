from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(5)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    # Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.


    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    print(people_radio.get_attribute("name"))  # Напечатает текстовое значение аттрибута name

    #assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    #print(people_radio.get_attribute("href"))
    # Напечатает None, т.к. аттрибут не существует. И это не строка, а None-значение.
    assert robots_checked is None, "Robot radio is not selected by default"
    print("value of robot radio: ", robots_checked)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_disabled = button.get_attribute("disabled")
    assert button_disabled is None, "Button is not disabled"
    print("value of button: ", button_disabled)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()