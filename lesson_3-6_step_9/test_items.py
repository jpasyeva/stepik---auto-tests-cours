import time
# Тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.

def test_add_cart_button_on_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    browser.find_element_by_css_selector('.add-to-basket .btn')
    check_text = browser.find_element_by_css_selector('.add-to-basket .btn').text
    assert check_text != None
