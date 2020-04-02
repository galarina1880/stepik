from selenium import webdriver
import time


# link = "http://suninjuly.github.io/simple_form_find_task.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link2)
    #
    # l = browser.find_element_by_link_text('224592')
    # l.click()

    field1 = browser.find_element_by_tag_name('input.form-control')
    field1.send_keys('Ivan')
    field2 = browser.find_element_by_name('last_name')
    field2.send_keys('Petrov')
    field3 = browser.find_element_by_class_name('city')
    field3.send_keys('Smolensk')
    field4 = browser.find_element_by_id('country')
    field4.send_keys('Russia')
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
