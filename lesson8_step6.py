import math
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


link = 'http://SunInJuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.set_window_position(0, 0)
    browser.set_window_size(1600, 1200)
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    chkbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", chkbox)
    chkbox.click()

    rbutton = browser.find_element_by_id('robotsRule')
    rbutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
