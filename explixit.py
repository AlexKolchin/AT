from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    browser.get(link)
    wait = WebDriverWait(browser, 12)
    element = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "$100"))
    book = browser.find_element(By.XPATH, "//*[@id='book']").click()
    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = int(x_element.text)
    result = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(result)
    submit = browser.find_element_by_xpath('//*[@id="solve"]').submit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

