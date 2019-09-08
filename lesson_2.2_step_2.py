from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим первое число
    find_num1 = browser.find_element_by_id("num1")
    # Находим текст внутри тега
    num1 = find_num1.text
    #Находим второе число
    find_num2 = browser.find_element_by_id("num2")
    num2 = find_num2.text
    # Считаем сумму и переводим посчитанную сумму в строку
    x = str(int(num1)+int(num2))
    # Выбираем полученное значение в выпадающем списке. При использовании данного метода не нужен выполнять click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x) #передаем значение х без кавычек. Кавчки означают что возьмется такое значение которое указанно в кавычках. А без ковычек значение посчитанное икса выше

    # Нажимаем кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


