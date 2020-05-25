# Фикстура открытия браузера
class OpenBrowser():
    def __init__(self, app):
        self.app = app

    def login_pos(self, user="iieikt266", passw="Stud?133"):
        wd = self.app.driver
        wd.get("http://open.kbsu.ru/moodle/")
        wd.find_element_by_name("username").send_keys("%s" % user)
        wd.find_element_by_name("password").send_keys(passw)
        wd.find_element_by_xpath("//input[@value='LOG IN']").click()
        wd.find_element_by_xpath("//a[contains(text(),'КУРСЫ')]").click()
        wd.find_element_by_xpath("//a[@id='label_2_2']/span").click()
        wd.find_element_by_xpath("//a[contains(text(),'Выход')]").click()

    def login_neg(self, user="iieikt266", passw="Stud?135"):
        wd = self.app.driver
        wd.get("http://open.kbsu.ru/moodle/")
        wd.find_element_by_name("username").send_keys("%s" % user)
        wd.find_element_by_name("password").send_keys(passw)
        wd.find_element_by_xpath("//input[@value='LOG IN']").click()
        elem = wd.find_element_by_xpath("//span[contains(.,'Вы не вошли в систему')]")
        assert elem.text == "Вы не вошли в систему"

    def login_empty(self, user="", passw=""):
        wd = self.app.driver
        wd.get("http://open.kbsu.ru/moodle/")
        wd.find_element_by_name("username").send_keys("%s" % user)
        wd.find_element_by_name("password").send_keys(passw)
        wd.find_element_by_xpath("//input[@value='LOG IN']").click()
        elem = wd.find_element_by_xpath("//span[contains(.,'Вы не вошли в систему')]")
        assert elem.text == "Вы не вошли в систему"










