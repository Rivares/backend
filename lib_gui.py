# coding: UTF-8

import lib_general as my_general

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.app import App

my_general.logging.getLogger('matplotlib.font_manager').disabled = True

root_path = my_general.root_path

path_name_ta_stocks = 'TA_stocks\\TA_stocks.py'
path_name_parser_stocks = 'Parser_market\\Parser_market.py'
market = []

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        img = Image(source='/path/to/real_python.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})

        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        # padding: Отступ padding между лейаутом и его дочерними элементами уточняется в пикселях.\
        # Для этого можно выбрать один из трех способов:
        # Список из четырех аргументов: [padding_left, padding_top, padding_right, padding_bottom]
        # Список из двух аргументов: [padding_horizontal, padding_vertical]
        # Один аргумент:
        # padding = 10 spacing: При помощи данного аргумента добавляется расстояние между дочерними виджетами.
        # orientation: Позволяет изменить значение orientation для BoxLayout по умолчанию — с горизонтального на вертикальное.

        for i in range(5):
            btn = Button(text="Button #%s" % (i + 1),
                         background_color=my_general.random.choice(colors),
                         size_hint=(.5, .5),
                         pos_hint={'center_x': .5, 'center_y': .5})

            btn.bind(on_press=self.on_press_button)

            layout.add_widget(btn)

    def on_press_button(self, instance):
        print('Вы нажали на кнопку!')

        return label
