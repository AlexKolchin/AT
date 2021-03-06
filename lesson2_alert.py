from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
link = 'http://suninjuly.github.io/alert_accept.html'
try:
    browser.get(link)
    first_button = browser.find_element_by_css_selector(".btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = int(x_element.text)
    result = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(result)
    submit = browser.find_element_by_css_selector('.btn.btn-primary').submit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
