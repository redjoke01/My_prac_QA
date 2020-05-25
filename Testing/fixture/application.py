from selenium import webdriver
from fixture.login import OpenBrowser

# Создал фикстуру инициализации
class Application():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.begin = OpenBrowser(self)









