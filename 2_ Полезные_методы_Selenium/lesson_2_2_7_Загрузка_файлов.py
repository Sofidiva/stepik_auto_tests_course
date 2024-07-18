'''import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)'''
import time

'''
print(os.path.abspath(__file__))                     
print(os.path.abspath(os.path.dirname(__file__)))   
'''

'''Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
Три способа задать путь к файлу:
#1. вбить руками
element.send_keys("/home/user/stepik/Chapter2/file_example.txt")

# 2. задать с помощью переменных
# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)
# отправляем файл
element.send_keys(file_path)
# 3.путь автоматизатора.
# если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
element.send_keys(file_path)
'''

# Итоговый код:
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # заполнение полей
    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first_name.send_keys('Ivan')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Ivanov')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('email.email')

    # загрузка файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    #1 file_name = "file_example.txt"
    #1 file_path = os.path.join(current_dir, file_name)

    #2 создаем файл
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    file_path = os.getcwd() + '/' + file.name

    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)

    #2 Удаляем созданный файл
    os.remove(file_path)

    # нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(3)
    browser.quit()