# coding: UTF-8

import lib_general as my_general
import lib_core as my_core

from backend_kivyagg import FigureCanvasKivyAgg

from kivy.core.window import Window

from kivy.properties import OptionProperty
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty

from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.app import App

my_general.logging.getLogger('matplotlib.font_manager').disabled = True

root_path = my_general.root_path

path_name_ta_stocks = 'TA_stocks\\TA_stocks.py'
path_name_parser_stocks = 'Parser_market\\Parser_market.py'
market = []

m_size_window_pass = (400, 200)
m_size_window_main = Window.system_size
m_size_window_3 = Window.system_size

Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: False
        touch_multiselect: True
<ExampleViewer>: 
    viewclass: 'Button'  # defines the viewtype for the data items. 
    orientation: "vertical"
    spacing: 40
    padding:10, 10
    space_x: self.size[0]/3
  
    RecycleBoxLayout: 
        color:(0, 0.7, 0.4, 0.8) 
        default_size: None, dp(56) 
  
        # defines the size of the widget in reference to width and height 
        default_size_hint: 0.4, None 
        size_hint_y: None
        height: self.minimum_height 
        orientation: 'vertical' # defines the orientation of data items
''')


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Login'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MainApp(App):

    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
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
        # # orientation: Позволяет изменить значение orientation для BoxLayout
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

        return label


class PasswordScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.size = m_size_window_pass

        boxlayout = BoxLayout(orientation="vertical", spacing=1, padding=[5])
        print("PasswordScreen")

        auth = LoginScreen()

        btn_sign_in = Button(
            text="Sign In",
            background_color=[255, 255, 255, 1],
            color=[0, 0, 0, 1],
            size_hint=[1, 0.3],
            on_press=self._on_press_button_sign_in,
        )

        boxlayout.add_widget(auth)
        boxlayout.add_widget(btn_sign_in)

        self.add_widget(boxlayout)

    def _on_press_button_sign_in(self, *args):
        # Checking ... TODO (1)
        # Window.toggle_fullscreen()
        Window.fullscreen = 'auto'
        self.manager.transition.direction = 'left'
        self.manager.current = 'MainScreen'


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print("MainScreen")

        gridlayout = GridLayout(cols=2, spacing=10)
        boxlayout_col_0 = BoxLayout(orientation="vertical", spacing=10)
        boxlayout_row_0 = BoxLayout(orientation="horizontal", spacing=10)
        boxlayout_col_1 = BoxLayout(orientation="vertical", spacing=10)
        boxlayout_row_1 = BoxLayout(orientation="horizontal", spacing=10)

        boxlayout_col_0.add_widget(Button(
            text="Glass",
            background_color=[.50, 0, 0, 1],
            size_hint_x=None,
            width=250,
        ))

        i = 0
        boxlayout_col_0_0 = BoxLayout(orientation="vertical", spacing=2)
        boxlayout_col_0_1 = BoxLayout(orientation="vertical", spacing=2)
        boxlayout_row_0_0 = BoxLayout(orientation="horizontal", spacing=2)
        slider = Slider(orientation='vertical', min=0, max=len(my_core.result_str_ticker),
                        value=len(my_core.result_str_ticker), step=1,
                        value_track=True, value_track_color=[1, 0, 0, 1])

        while i < len(my_core.result_str_ticker)-60:
            boxlayout_col_0_0.add_widget(Button(
                text=my_core.result_str_ticker[i],
                font_size='14',
                # text_size=(None, None),
                background_color=[0, .50, 0, 1],
                size_hint_x=None,
                height=100,
                width=250,
            ))

            i += 1

        boxlayout_col_0_1.add_widget(slider)
        boxlayout_col_0_1.size_hint_x = 0.05

        boxlayout_row_0_0.add_widget(boxlayout_col_0_0)
        boxlayout_row_0_0.add_widget(boxlayout_col_0_1)
        boxlayout_col_0.add_widget(boxlayout_row_0_0)

        gridlayout.add_widget(boxlayout_col_0)

        boxlayout_row_0.add_widget(Button(
            text="Doubler Screen -->",
            background_color=[0, 1, 0, 1],
            on_press=self._on_press_button_to_doubler_screen,
            width=250,
        ))

        boxlayout_row_0.add_widget(Button(
            text="Sign out",
            background_color=[1, 0, 0, 1],
            on_press=self._on_press_button_sign_out,
            width=250,
        ))
        boxlayout_row_0.height = 50
        boxlayout_row_0.size_hint = [1, 0.1]
        boxlayout_col_1.add_widget(boxlayout_row_0)

        my_general.plt.plot([1, 23, 2, 4])
        my_general.plt.ylabel('some numbers')

        boxlayout_col_1.add_widget(FigureCanvasKivyAgg(my_general.plt.gcf()))
        boxlayout_col_1.size_hint_x = None
        boxlayout_col_1.size_hint_y = 200
        boxlayout_col_1.width = 1750
        boxlayout_col_1.height = 700
        gridlayout.add_widget(boxlayout_col_1)

        gridlayout.add_widget(Button(
            text="Deferred orders",
            background_color=[0, 0, .50, 1],
            size_hint_x=None,
            width=250,
        ))

        boxlayout_row_1.add_widget(Button(
            text="Active orders",
            background_color=[0, .50, 0, 1],
        ))

        boxlayout_row_1.add_widget(Button(
            text="Explanations for notes",
            background_color=[0, 0, .50, 1],
        ))
        boxlayout_row_1.size_hint = [1, None]
        gridlayout.add_widget(boxlayout_row_1)

        self.add_widget(gridlayout)

    def _on_press_button_to_doubler_screen(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'DoublerScreen'

    def _on_press_button_sign_out(self, *args):
        Window.fullscreen = False
        # Window.toggle_fullscreen()  # Deprecated
        Window.size = m_size_window_pass
        self.manager.transition.direction = 'right'
        self.manager.current = 'PasswordScreen'


class DoublerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print("DoublerScreen")

        gridlayout = GridLayout(cols=2, spacing=10)
        boxlayout_col_0 = BoxLayout(orientation="vertical", spacing=10)
        boxlayout_row_0 = BoxLayout(orientation="horizontal", spacing=10)
        boxlayout_col_1 = BoxLayout(orientation="vertical", spacing=10)
        boxlayout_row_1 = BoxLayout(orientation="horizontal", spacing=10)

        boxlayout_col_0.add_widget(Button(
            text="Glass",
            background_color=[.50, 0, 0, 1],
            size_hint_x=None,
            width=250,
        ))

        boxlayout_col_0.add_widget(Button(
            text="List assets",
            background_color=[0, .50, 0, 1],
            size_hint_x=None,
            width=250,
        ))
        gridlayout.add_widget(boxlayout_col_0)

        boxlayout_row_0.add_widget(Button(
            text="<-- Main Screen",
            background_color=[0, 1, 0, 1],
            on_press=self._on_press_button_to_main_screen,
            width=250,
        ))

        boxlayout_row_0.add_widget(Button(
            text="Sign out",
            background_color=[1, 0, 0, 1],
            on_press=self._on_press_button_sign_out,
            width=250,
        ))
        boxlayout_row_0.height = 50
        boxlayout_row_0.size_hint = [1, 0.1]
        boxlayout_col_1.add_widget(boxlayout_row_0)

        my_general.plt.plot([1, 23, 2, 4])
        my_general.plt.ylabel('some numbers')

        boxlayout_col_1.add_widget(FigureCanvasKivyAgg(my_general.plt.gcf()))
        boxlayout_col_1.size_hint_x = None
        boxlayout_col_1.size_hint_y = 200
        boxlayout_col_1.width = 1750
        boxlayout_col_1.height = 700
        gridlayout.add_widget(boxlayout_col_1)

        gridlayout.add_widget(Button(
            text="Deferred orders",
            background_color=[0, 0, .50, 1],
            size_hint_x=None,
            width=250,
        ))

        boxlayout_row_1.add_widget(Button(
            text="Active orders",
            background_color=[0, .50, 0, 1],
        ))

        boxlayout_row_1.add_widget(Button(
            text="Explanations for notes",
            background_color=[0, 0, .50, 1],
        ))
        boxlayout_row_1.size_hint = [1, None]
        gridlayout.add_widget(boxlayout_row_1)

        self.add_widget(gridlayout)

    def _on_press_button_to_main_screen(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'

    def _on_press_button_sign_out(self, *args):
        Window.fullscreen = False
        # Window.toggle_fullscreen()  # Deprecated
        Window.size = m_size_window_pass
        self.manager.transition.direction = 'right'
        self.manager.current = 'PasswordScreen'


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': my_core.result_str_ticker[i]} for i in range(len(my_core.result_str_ticker))]


class TestApp(App):
    def build(self):
        return RV()


# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# Kivy Example App for the slider widget
from kivy.app import App

# The GridLayout arranges children in a matrix.
from kivy.uix.gridlayout import GridLayout

# If we will not import this module
# It will through the error
from kivy.uix.slider import Slider

# The Label widget is for rendering text.
from kivy.uix.label import Label

# Property that represents a numeric value
# within a minimum bound and / or maximum
# bound – within a numeric range.
from kivy.properties import NumericProperty


# class in which we are defining the
# sliders and its effects
class WidgetContainer(GridLayout):

    def __init__(self, **kwargs):
        # super function can be used to gain access
        # to inherited methods from a parent or sibling
        # class that has been overwritten in a class object.
        super(WidgetContainer, self).__init__(**kwargs)

        # 4 columns in grid layout
        self.cols = 4

        # declaring the slider and adding some effects to it
        self.brightnessControl = Slider(min=0, max=100)

        # 1st row - one label, one slider
        self.add_widget(Label(text='brightness'))
        self.add_widget(self.brightnessControl)

        # 2nd row - one label for caption,
        # one label for slider value
        self.add_widget(Label(text='Slider Value'))
        self.brightnessValue = Label(text='0')
        self.add_widget(self.brightnessValue)

        # On the slider object Attach a callback
        # for the attribute named value
        self.brightnessControl.bind(value=self.on_value)

        # Adding functionality behind the slider

    # i.e when pressed increase the value
    def on_value(self, instance, brightness):
        self.brightnessValue.text = "% d" % brightness

    # The app class


class SliderExample(App):
    def build(self):
        widgetContainer = WidgetContainer()
        return widgetContainer

    # creating the object root for ButtonApp() class



# Define the Recycleview class which is created in .kv file
class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]

    # Create the App class with name of your app.


class SampleApp(App):
    def build(self):
        return ExampleViewer()


class Investment_analysis(App):

    def build(self):
        # sm = ScreenManager()

        # root = SliderExample()
        # root.run()

        SampleApp().run()

        # sm.add_widget(PasswordScreen(name='PasswordScreen'))
        # sm.add_widget(MainScreen(name='MainScreen'))
        # sm.add_widget(DoublerScreen(name='DoublerScreen'))
        #
        # return sm
