import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

'''
def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser, request): 
   language = request.config.getoption("--language")
   link = f"http://selenium1py.pythonanywhere.com/{language}/"
   browser.get(link) 
   go_to_login_page(browser) 
'''

def test_guest_can_go_to_login_page(browser, request):
    language = request.config.getoption("--language")
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_link()      # проверяем наличие ссылки
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    
