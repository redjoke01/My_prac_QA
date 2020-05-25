class Header:
    def __init__(self, app):
        self.app = app

    def login_pos(self, user="iieikt266", passw="Stud?133"):
        wd = self.app.driver
        wd.get("http://open.kbsu.ru/moodle/")
        wd.find_element_by_name("username").send_keys("%s" % user)
        wd.find_element_by_name("password").send_keys(passw)
        wd.find_element_by_xpath("//input[@value='LOG IN']").click()

    def head_menu(self):
        wd = self.app.driver
        wd.find_element_by_xpath("//a[contains(text(),'ГЛАВНАЯ')]").click()
        wd.find_element_by_xpath("// a[contains(text(), 'О НАС')]").click()
        title_01 = wd.title
        assert title_01 == "О НАС"
        wd.find_element_by_xpath("//a[contains(text(),'КУРСЫ')]").click()
        title_02 = wd.title
        assert title_02 == "OpenKBSU: Категории курсов"
        wd.find_element_by_xpath("// a[contains(text(), 'ДОКУМЕНТЫ')]").click()
        title_03 = wd.title
        assert title_03 == "Документы"
        wd.find_element_by_xpath("//a[contains(text(),'ПОМОЩЬ')]").click()
        title_04 = wd.title
        assert title_04 == "Справка"
        wd.find_element_by_xpath("//a[contains(text(),'ПОИСК')]").click()
        title_05 = wd.title
        assert title_05 == "Открытый университет - OpenKBSU : Найти"
        wd.find_element_by_id("coursesearchbox").send_keys("Анкетирование")
        wd.find_element_by_xpath("//input[@value='Применить']").click()
        res = wd.find_element_by_xpath("//h2[contains(.,'Результаты поиска: 18')]").text
        assert res == "Результаты поиска: 18"
        print("\n" + res)








