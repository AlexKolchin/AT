from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit_button")
#button = browser.find_element(By.ID, "submit_button")
print(button)
button.click()

browser.close() # закрывает текущее окно браузера
browser.quit() # закрывает браузер полностью