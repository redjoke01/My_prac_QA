from selenium import webdriver
from fixture.login import OpenBrowser
from fixture.check_header import Header

# Создал фикстуру инициализации
class Application():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.begin = OpenBrowser(self)
        self.header = Header(self)
















