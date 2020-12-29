# coding: UTF-8

import lib_general as my_general
import lib_core as my_core

from backend_kivyagg import FigureCanvasKivyAgg

from kivy.core.window import Window
from kivy.properties import OptionProperty

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.app import App
from kivy.utils import hex_colormap, get_color_from_hex
from kivy.metrics import dp


class ExRV(RecycleView):
    def __init__(self, **kwargs):
        super(ExRV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]


class Investment_analysis(App):
    def build(self):
        return ExRV()


# class Investment_analysis(App):
#
#     def build(self):
#         sm = ScreenManager()
#
#         # sm.add_widget(PasswordScreen(name='PasswordScreen'))
#         # sm.add_widget(MainScreen(name='MainScreen'))
#         # sm.add_widget(DoublerScreen(name='DoublerScreen'))
#
#         return sm
