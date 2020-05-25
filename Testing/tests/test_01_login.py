import pytest
from fixture.application import Application

# Вызвал фикстуру инициализации
@pytest.fixture(scope = "session")
def app():
    fixture = Application()
    return fixture

# Вызвал фикстуры проверки логина
def test_01_positive(app):
    app.begin.login_pos()

def test_02_negative(app):
    app.begin.login_neg()

def test_03_empty(app):
    app.begin.login_empty()













