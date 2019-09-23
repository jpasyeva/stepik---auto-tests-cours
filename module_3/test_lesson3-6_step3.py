import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Задаем фикстуру для подсчета ответа, чтобы в каждом новом тесте был актуальный ответ
@pytest.fixture(scope='function')
def answer():
    return str(math.log(int(time.time())))

#задаем фикстуру открытия-закрытия браузера и выполнения тестов в рамках одного браузера
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    #Настройка ожидания для поиска элемента (5сек)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

# Передаем параметры ссылок, которые различаются
testDataLink = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

@pytest.mark.parametrize('step', testDataLink)
class TestLinkStep(object):
    # вызываем фикстуры в тесте, передав их как параметры
    def test_link_step(self, browser, step, answer):
        # Открываем ссылку
        link = f"https://stepik.org/lesson/{step}/step/1"
        browser.get(link)
        #Ищем поле для ввода ответа и вводим ответ
        input_answer = browser.find_element_by_css_selector(".textarea")
        input_answer.send_keys(answer)
        #Ищем и нажимаем кнопку отправить
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        # Ждем сообщения о правильности ответа
        # говорим Selenium проверять в течение 10 секунд, пока не появится нужный текст
        Find_massage = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"),"Correct!"))
        
