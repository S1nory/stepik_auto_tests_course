from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    for element in elements:
        element.send_keys("Мой ответ")
        time.sleep(10)
    # Ваш код, который заполняет обязательные поля
    #input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
    #input1.send_keys("Ivan")
    #time.sleep(10)
    #input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
    #input2.send_keys("Petrov")
    #time.sleep(10)
    #input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    #input3.send_keys("xui")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

