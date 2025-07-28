import time
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_cart_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    # time.sleep(3)  # можно раскомментировать для ручной проверки
    add_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_button, "Кнопка добавления в корзину не найдена"

