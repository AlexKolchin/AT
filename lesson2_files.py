from selenium import webdriver
import math
import time
import os
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
link = 'http://suninjuly.github.io/file_input.html'
try:
    browser.get(link)
    firstname = browser.find_element_by_xpath("//*[@name='firstname']").send_keys('FirstName')
    lasttname = browser.find_element_by_xpath("//*[@name='lastname']").send_keys('LastName')
    email = browser.find_element_by_xpath("//*[@name='email']").send_keys('Email')
    download = browser.find_element_by_xpath("//*[@id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    download.send_keys(current_dir)
    submit = browser.find_element_by_css_selector('.btn.btn-primary').submit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
