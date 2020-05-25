# Вызвал фикстуру проверки шапки сайта
import pytest
from fixture.application import Application

@pytest.fixture(scope = "session")
def app():
    fixture = Application()
    return fixture

def test_check_hedmenu(app):
    app.header.login_pos()
    app.header.head_menu()

