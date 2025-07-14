from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    





    
    #find element
    #gold_path = browser.find_element(By.ID, "treasure")
    #find attribute
    #gold_val = gold_path.get_attribute("valuex")
    #print("value hagues: ", gold_val)
    #assert gold_val is not None, "People radio is not selected by default"

    #find first number
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    #find second number
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    #find sum
    res = int(x)+int(y) 
    print(res)
    
    #выбираем нужное и кликаем по нему 
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f"option[value='{res}']").click()





    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

