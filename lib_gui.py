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

Builder.load_file('.\\gui\\ExampleViewer.kv')


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

        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(100):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)

        # runTouchApp(root)

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

        boxlayout_row_0_0.add_widget(root)
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

class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]


class MyViewer(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.viewclass = 'Button'  # defines the viewtype for the data items.
        self.orientation = "vertical"
        self.spacing = 40
        self.padding = (10, 10)
        self.space_x = self.size[0]/3


class TestApp(App):
    def build(self):
        return ExampleViewer()


class Investment_analysis(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(PasswordScreen(name='PasswordScreen'))
        sm.add_widget(MainScreen(name='MainScreen'))
        sm.add_widget(DoublerScreen(name='DoublerScreen'))

        return sm
