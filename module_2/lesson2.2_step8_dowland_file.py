from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # имя
    input_name = browser.find_element_by_name("firstname")
    input_name.send_keys('My name')
    # фамилия
    input_lastname = browser.find_element_by_name("lastname")
    input_lastname.send_keys('My last name')
    # почта
    input_email = browser.find_element_by_name("email")
    input_email.send_keys('test@test.io')
    # загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'julia.txt')           # добавляем к этому пути имя файла
    element =  browser.find_element_by_id("file") #находим элемент кнопку добавления файла
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

