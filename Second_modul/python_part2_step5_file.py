from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    #заполняем поля 
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Ivan")
    

    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys("Ivanov")
    

    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("Ivanov@pes.com")
   

    input4 = browser.find_element(By.CSS_SELECTOR, '[name="file"]')

    #нахожу путь к текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)

    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'file.txt')

    #прикрепляем файл
    input4.send_keys(file_path)

      

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
