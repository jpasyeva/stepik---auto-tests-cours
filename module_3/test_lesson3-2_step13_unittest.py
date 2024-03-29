import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
    def test_rega1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_xpath('//form/div[1]/div[1]/input').send_keys('vvv')
        browser.find_element_by_xpath('//form/div[1]/div[2]/input').send_keys('rrr')
        browser.find_element_by_xpath('//form/div[1]/div[3]/input').send_keys('wwyandex.ru')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # закрываем браузер после всех манипуляций
        browser.quit()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "something went wrong")

    def test_rega2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_xpath('//form/div[1]/div[1]/input').send_keys('vvv')
        browser.find_element_by_xpath('//form/div[1]/div[2]/input').send_keys('rrr')
        browser.find_element_by_xpath('//form/div[1]/div[3]/input').send_keys('wwyandex.ru')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # закрываем браузер после всех манипуляций
        browser.quit()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "something went wrong")

if __name__ == "__main__":
    unittest.main()
