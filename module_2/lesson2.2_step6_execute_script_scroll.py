from selenium import webdriver
import time
import math

# Код для вычислния формулы на странице
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение переменной х
    x_element = browser.find_element_by_css_selector("#input_value")
    # Присваеваем найденное значение переменной х
    x = x_element.text
    # Считаем у
    y = calc(x)
    # Скроллим страницу вниз.
    input = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    # Ввод у в текстовое поле
    #input_answer = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    # Выбраем radiobutton "Robots rule!"
    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()

    # Скролим до кнопки и отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


