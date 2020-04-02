from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    field1 = browser.find_element_by_name('firstname')
    field1.send_keys('Ivan')
    field2 = browser.find_element_by_name('lastname')
    field2.send_keys('Petrov')
    field3 = browser.find_element_by_name('email')
    field3.send_keys('Smolensk')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson8_step8.txt')
    file = browser.find_element_by_id('file')
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
