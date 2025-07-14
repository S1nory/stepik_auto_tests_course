from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import os 
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element(By.ID, "button")


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
