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




    #Теперь рассмотрим ситуацию, когда в сценарии теста возникает необходимость не только получить содержимое alert, но и нажать кнопку OK, чтобы закрыть alert. Alert является модальным окном: это означает, что пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert. Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды accept():

    alert = browser.switch_to.alert
    alert.accept()
    #Чтобы получить текст из alert, используйте свойство text объекта alert:

    alert = browser.switch_to.alert
    alert_text = alert.text
    #Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm. Для переключения на окно confirm используется та же команда, что и в случае с alert:

    confirm = browser.switch_to.alert
    confirm.accept()

    #Для confirm-окон можно использовать следующий метод для отказа:

    confirm.dismiss()
    #То же самое, что и при нажатии пользователем кнопки "Отмена". 

    #Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():

    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()


    # Находим элемент, в котором нужно проверить текст.
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "price"))
    )
    #задаем нужный текст
    expected_text = "$100"

    # Используем явное ожидание, чтобы убедиться, что элемент загрузился с нужным текстом.
    element_text = WebDriverWait(driver, 10).until(
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
