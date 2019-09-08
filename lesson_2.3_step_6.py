from selenium import webdriver
import time
import math

# Код для вычислния формулы на странице
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Нажимем на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Считываем значение переменной х
    x_element = browser.find_element_by_css_selector("#input_value")
    # Присваеваем найденное значение переменной х
    x = x_element.text
    # Считаем у
    y = calc(x)
    # Ввод у в текстовое поле
    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


