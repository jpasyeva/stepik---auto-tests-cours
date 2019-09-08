from selenium import webdriver
import time
import math

# Код для вычислния формулы на странице
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент картинку
    find_img = browser.find_element_by_id("treasure")
    # Берем значение атрибута у картинки и присваем это значение иксу
    x = find_img.get_attribute("valuex")

    # Считываем значение переменной х
    #x_element = browser.find_element_by_css_selector("#input_value")
    # Присваеваем найденное значение переменной х
    #x = x_element.text
    # Считаем у
    y = calc(x)
    # Ввод у в текстовое поле
    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)
    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    # Выбраем radiobutton "Robots rule!"
    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


