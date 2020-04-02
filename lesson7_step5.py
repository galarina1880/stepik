import math
from selenium import webdriver
import time


link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id('treasure')
    x = chest.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    chkbox = browser.find_element_by_id('robotCheckbox')
    chkbox.click()

    rbutton = browser.find_element_by_id('robotsRule')
    rbutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
