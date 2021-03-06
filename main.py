from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder



Builder.load_string("""

<Test>:
    
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'Понедельник'
        Label:
            font_size: 45
            text:
                '\\n'.join((app.otstup+"Понедельник", app.sepLine,
                "1 Урок - География", app.sepLine,
                "2 Урок - Украинский язык", app.sepLine,
                "3 Урок - Математика", app.sepLine,
                "4 Урок - Английский язык", app.sepLine,
                "5 Урок - Немецкий язык", app.sepLine,
                "6 Урок - Труды", app.sepLine,
                "7 Урок - Физ-ра", app.sepLine))        
    TabbedPanelItem:
        text: 'Вторник'               
        Label:
            font_size: 45
            text:
                '\\n'.join((app.otstup+"Вторник", app.sepLine,
                "1 Урок - Зарубежная Лит-ра", app.sepLine,
                "2 Урок - Английский язык", app.sepLine,
                "3 Урок - Украинский язык", app.sepLine,
                "4 Урок - Информатика", app.sepLine,
                "5 Урок - История", app.sepLine,
                "6 Урок - Математика", app.sepLine,
                "7 Урок - ОТМ / Пусто", app.sepLine))
           
    TabbedPanelItem:
        text: 'Среда'
        Label:
            font_size: 45
            text:
                '\\n'.join((app.otstup+"Среда", app.sepLine,
                "1 Урок - Математика", app.sepLine,
                "2 Урок - Физ-ра", app.sepLine,
                "3 Урок - Английский язык", app.sepLine,
                "4 Урок - Украинская Лит-ра", app.sepLine,
                "5 Урок - Биология", app.sepLine,
                "6 Урок - Русский язык", app.sepLine,
                "7 Урок - История", app.sepLine))
    TabbedPanelItem:
        text: 'Четверг'
        Label:
            font_size: 45
            text:
                '\\n'.join((app.otstup+"Четверг", app.sepLine,
                "1 Урок - Английский язык", app.sepLine,
                "2 Урок - Украиский язык", app.sepLine,
                "3 Урок - Немеций язык", app.sepLine,
                "4 Урок - Физ-ра", app.sepLine,
                "5 Урок - Основы здоровья", app.sepLine,
                "6 Урок - География", app.sepLine))
    TabbedPanelItem:
        text: 'Пятница'
        Label:
            font_size: 45
            text:
                '\\n'.join((app.otstup+"Пятница", app.sepLine,
                "1 Урок - Укр. мов / Музика", app.sepLine,
                "2 Урок - Математика", app.sepLine,
                "3 Урок - Труды", app.sepLine,
                "4 Урок - Биология", app.sepLine,
                "5 Урок - Украинский язык", app.sepLine,
                "6 Урок - Зарубежная Лит-ра", app.sepLine,
                "7 Урок - Английский язык", app.sepLine))
    TabbedPanelItem:
        text: 'Расписание'
        Label:
            font_size: 45
            text:
                '\\n'.join((app.miniotstup+"Распис. времени уроков", app.sepLine,
                "1 Урок - 8:00 - 8:45", app.sepLine,
                "2 Урок - 8:55 - 9:40", app.sepLine,
                "3 Урок - 10:00 - 10:45", app.sepLine,
                "4 Урок - 11:05 - 11:50", app.sepLine,
                "5 Урок - 12:00 - 12:45", app.sepLine,
                "6 Урок - 12:55 - 13:40", app.sepLine,
                "7 Урок - 13:50 - 14:35", app.sepLine))
    TabbedPanelItem:
        text: 'Перемены'
        Label:
            font_size: 45
            text:
                '\\n'.join((app.miniotstup+"Перемен между уроками", app.sepLine,
                "1 Урок - 8:45 - 8:55", app.sepLine,
                "2 Урок - 9:40 - 10:00", app.sepLine,
                "3 Урок - 10:45 - 11:05", app.sepLine,
                "4 Урок - 11:50 - 12:00", app.sepLine,
                "5 Урок - 12:45 - 12:55", app.sepLine,
                "6 Урок - 13:40 - 13:50", app.sepLine,
                "7 Урок - 14:35 - 14:45", app.sepLine))
""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    sepLine = "-" * 50
    otstup = " "*15
    miniotstup = " "*3
    def build(self):
        return Test()


if __name__ == '__main__':
    TabbedPanelApp().run()