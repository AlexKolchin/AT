from selenium import webdriver
import time

site = 'http://suninjuly.github.io/find_xpath_form'
try:
    browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    browser.get(site)
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]v')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла