import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавление обработчика, который считывает из командной строки параметр language.
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")

# Логика запуска браузера с указанным языком пользователя.
#Браузер объявляется в фикстуре browser и передается в тест как параметр.
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language != None:
        print("\nstart page..")
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--don't choose language")
    yield browser
    print("\nquit browser..")
    browser.quit()
