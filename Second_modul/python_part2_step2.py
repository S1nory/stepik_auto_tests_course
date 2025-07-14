from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #input func
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    #find element
    gold_path = browser.find_element(By.ID, "treasure")
    #find attribute
    gold_val = gold_path.get_attribute("valuex")
    print("value hagues: ", gold_val)
    assert gold_val is not None, "People radio is not selected by default"


    #x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    #x = x_element.text
    y = calc(gold_val)


    #находим текстовое поле и вводим ответ
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    

    #Ставим галочку о том что мы робот 
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

