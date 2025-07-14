from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import os 
import math

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("https://suninjuly.github.io/explicit_wait2.html")


    # Находим элемент, в котором нужно проверить текст.
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "price"))
    )
    #задаем нужный текст
    expected_text = "$100"

    # Используем явное ожидание, чтобы убедиться, что элемент загрузился с нужным текстом.
    element_text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), expected_text)
    )

    
    #click to button
    button = browser.find_element(By.ID, "book")
    button.click()

   
    #input func
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)


    #находим текстовое поле и вводим ответ
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    #проверяем загрузку кнопки и кликаем по ней 

    button2 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )

    button2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
