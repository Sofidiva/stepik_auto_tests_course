from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    # Модальное окно. alert - только принятие
    alert = browser.switch_to.alert             # переключение на модальное окно
    alert.accept()                              # принятие

    # Модальное окно. confirm - принятие и отказ
    confirm = browser.switch_to.alert             # переключение на модальное окно
    confirm.accept()                              # принятие
    confirm.dismiss()                             # отказ

    # Модальное окно. prompt - принятие и отказ + ввод текста
    prompt = browser.switch_to.alert             # переключение на модальное окно
    prompt.send_keys("My answer")                # ввод текста
    prompt.accept()                              # принятие
    prompt.dismiss()                             # отказ



finally:
    time.sleep(2)
    browser.quit()