from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

driver.get('https://translate.google.com/')

print(driver.title) #title of the page

driver.close() # close browser
