# coding: UTF-8

import lib_general as my_general
from backend_kivyagg import FigureCanvasKivyAgg

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
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

my_general.plt.plot([1, 23, 2, 4])
my_general.plt.ylabel('some numbers')

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MainApp(App):
    def build(self):
        # label = Label(text='Hello from Kivy',
        #               size_hint=(.5, .5),
        #               pos_hint={'center_x': .5, 'center_y': .5})
        #
        # img = Image(source='/path/to/real_python.png',
        #             size_hint=(1, .5),
        #             pos_hint={'center_x': .5, 'center_y': .5})
        #
        # layout = BoxLayout(padding=10)
        # colors = [red, green, blue, purple]
        #
        # # padding: Отступ padding между лейаутом и его дочерними элементами уточняется в пикселях.\
        # # Для этого можно выбрать один из трех способов:
        # # Список из четырех аргументов: [padding_left, padding_top, padding_right, padding_bottom]
        # # Список из двух аргументов: [padding_horizontal, padding_vertical]
        # # Один аргумент:
        # # padding = 10 spacing: При помощи данного аргумента добавляется расстояние между дочерними виджетами.
        # # orientation: Позволяет изменить значение orientation для BoxLayout по умолчанию — с горизонтального на вертикальное.
        #
        # for i in range(5):
        #     btn = Button(text="Button #%s" % (i + 1),
        #                  background_color=my_general.random.choice(colors),
        #                  size_hint=(.5, .5),
        #                  pos_hint={'center_x': .5, 'center_y': .5})
        #
        #     btn.bind(on_press=self.on_press_button)
        #
        #     layout.add_widget(btn)
        #
        #     self.operators = ["/", "*", "+", "-"]
        #     self.last_was_operator = None
        #     self.last_button = None
        #     main_layout = BoxLayout(orientation="vertical")
        #     self.solution = TextInput(
        #         multiline=False, readonly=True, halign="right", font_size=55
        #     )
        #     main_layout.add_widget(self.solution)
        #     buttons = [
        #         ["7", "8", "9", "/"],
        #         ["4", "5", "6", "*"],
        #         ["1", "2", "3", "-"],
        #         [".", "0", "C", "+"],
        #     ]
        #     for row in buttons:
        #         h_layout = BoxLayout()
        #         for label in row:
        #             button = Button(
        #                 text=label,
        #                 pos_hint={"center_x": 0.5, "center_y": 0.5},
        #             )
        #             button.bind(on_press=self.on_button_press)
        #             h_layout.add_widget(button)
        #         main_layout.add_widget(h_layout)
        #
        #     equals_button = Button(
        #         text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        #     )
        #     equals_button.bind(on_press=self.on_solution)
        #     main_layout.add_widget(equals_button)
        #
        #     return main_layout
        #
        # def on_button_press(self, instance):
        #     current = self.solution.text
        #     button_text = instance.text
        #
        #     if button_text == "C":
        #         # Очистка виджета с решением
        #         self.solution.text = ""
        #     else:
        #         if current and (
        #             self.last_was_operator and button_text in self.operators):
        #             # Не добавляйте два оператора подряд, рядом друг с другом
        #             return
        #         elif current == "" and button_text in self.operators:
        #             # Первый символ не может быть оператором
        #             return
        #         else:
        #             new_text = current + button_text
        #             self.solution.text = new_text
        #     self.last_button = button_text
        #     self.last_was_operator = self.last_button in self.operators

        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(my_general.plt.gcf()))

        return box

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

    def on_press_button(self, instance):
        print('Вы нажали на кнопку!')
