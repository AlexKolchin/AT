from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
link = 'http://suninjuly.github.io/selects2.html'
try:
    browser.get(link)
    x_element = browser.find_element_by_xpath('//*[@id="num1"]')
    y_element = browser.find_element_by_xpath('//*[@id="num2"]')
    x = x_element.text
    y = y_element.text
    sum = int(x) + int(y)
    str_sum = str(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str_sum)
    submit = browser.find_element_by_css_selector('.btn.btn-default').submit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
