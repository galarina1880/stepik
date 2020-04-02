import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector('[id="num1"]').text
    y = browser.find_element_by_css_selector('[id="num2"]').text
    res = str(int(x) + int(y))

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(res)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
