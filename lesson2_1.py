from selenium import webdriver
import math
import time

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
link = 'http://suninjuly.github.io/math.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser.get(link)
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)
    checkbox = browser.find_element_by_css_selector("[id ='robotCheckbox']").click()
    radio = browser.find_element_by_css_selector("[for='robotsRule']").click()
    submit = browser.find_element_by_css_selector('.btn.btn-default').submit()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
