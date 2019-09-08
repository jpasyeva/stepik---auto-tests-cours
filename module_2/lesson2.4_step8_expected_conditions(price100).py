from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Код для вычислния формулы на странице
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)
    # говорим Selenium проверять в течение 12 секунд, пока цена не станет 100
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
    # нажимаем кнопку
    button = browser.find_element_by_id("book")
    button.click()


    # Считываем значение переменной х
    x_element = browser.find_element_by_css_selector("#input_value")
    # Присваеваем найденное значение переменной х
    x = x_element.text
    # Считаем у
    y = calc(x)
    # Ввод у в текстовое поле
    input_answer = browser.find_element_by_css_selector("#answer")
    input_answer.send_keys(y)

    # Скроллим и отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
