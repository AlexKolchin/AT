from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
link = 'http://SunInJuly.github.io/execute_script.html'
try:
    browser.get(link)
    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = int(x_element.text)
    result = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(result)
    assert True
    checkbox = browser.find_element_by_css_selector("[id ='robotCheckbox']").click()
    radio = browser.find_element_by_css_selector("[id='robotsRule']").click()
    submit = browser.find_element_by_css_selector('.btn.btn-primary').submit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
