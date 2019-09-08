from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
