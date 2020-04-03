import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fname = browser.find_element_by_css_selector('div.first_block > div.form-group.first_class > input')
        fname.send_keys('Ivan')
        sname = browser.find_element_by_css_selector('div.first_block > div.form-group.second_class > input')
        sname.send_keys('Petrov')
        email = browser.find_element_by_css_selector('div.first_block > div.form-group.third_class > input')
        email.send_keys('test@test.ru')

        time.sleep(10)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration successful!")
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        fname = browser.find_element_by_css_selector('div.first_block > div.form-group.first_class > input')
        fname.send_keys('Ivan')
        sname = browser.find_element_by_css_selector('div.first_block > div.form-group.second_class > input')
        sname.send_keys('Petrov')
        email = browser.find_element_by_css_selector('div.first_block > div.form-group.third_class > input')
        email.send_keys('test@test.ru')

        time.sleep(10)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Some elements are missing!")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
