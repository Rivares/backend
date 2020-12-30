# coding: UTF-8

import lib_general as my_general
import lib_core as my_core

from backend_kivyagg import FigureCanvasKivyAgg

from kivy.core.window import Window
from kivy.clock import Clock

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

from functools import partial

my_general.logging.getLogger('matplotlib.font_manager').disabled = True

root_path = my_general.root_path

path_name_ta_stocks = 'TA_stocks\\TA_stocks.py'
path_name_parser_stocks = 'Parser_market\\Parser_market.py'
market = []

m_size_window_pass = (400, 200)
m_size_window_main = Window.system_size
m_size_window_3 = Window.system_size

# Builder.load_file('.\\gui\\ExampleViewer.kv')

# Empty portfolio
my_portfolio = my_core.Portfolio()

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

    gridlayout = GridLayout(cols=2, spacing=10)
    current_graph = FigureCanvasKivyAgg(my_general.plt.gcf())
    boxlayout_col_0_0_0 = BoxLayout()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print("MainScreen")

        gridlayout = self.gridlayout
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

        boxlayout_col_0_0_0 = self.boxlayout_col_0_0_0
        boxlayout_col_0_1 = BoxLayout(orientation="vertical", spacing=2)
        boxlayout_row_0_0 = BoxLayout(orientation="horizontal", spacing=2)
        slider = Slider(orientation='vertical', min=0, max=len(my_core.result_str_ticker),
                        value=len(my_core.result_str_ticker), step=1,
                        value_track=True, value_track_color=[1, 0, 0, 1])

        boxlayout_col_0_0 = GridLayout(cols=1, spacing=2, size_hint_y=5)
        boxlayout_col_0_0.bind(minimum_height=boxlayout_col_0_0.setter('height'))
        i = 0
        while i < len(my_core.result_str_ticker):
            boxlayout_col_0_0.add_widget(Button(
                text=my_core.result_str_ticker[i],
                font_size='14',
                background_color=[0, .50, 0, 1],
                size_hint_x=None,
                height=10,
                width=250,
                on_press=partial(self._on_press_change_ticker, my_core.result_str_ticker[i]),
            ))

            i += 1

        boxlayout_col_0_1.add_widget(slider)
        boxlayout_col_0_1.size_hint_x = 0.05

        scroll_view = ScrollView()
        scroll_view.add_widget(boxlayout_col_0_0)

        boxlayout_row_0_0.add_widget(scroll_view)
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
        boxlayout_col_0_0_0.add_widget(self.current_graph)

        boxlayout_col_1.add_widget(boxlayout_col_0_0_0)
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

    def _on_press_change_ticker(self, l_result_str_ticker, *args):
        print(l_result_str_ticker)
        # my_portfolio.print_graph_(list_name_tickers=[l_result_str_ticker], depart_market='STCK',
        #                           list_name_indicators=[''],
        #                           user_start_moment=my_general.datetime.date(my_general.datetime.datetime.now().year, 1, 1),
        #                           user_end_moment=my_general.datetime.date(my_general.datetime.datetime.now().year,
        #                                                                    my_general.datetime.datetime.now().month,
        #                                                                    my_general.datetime.datetime.now().day),
        #                           user_time_frame='HOURLY')
        print("print_graph_")
        my_general.plt.clf()
        self.gridlayout.remove_widget(self.current_graph)

        my_general.plt.plot([1, 2, 2, 4])
        my_general.plt.ylabel('some numbers')
        self.current_graph = FigureCanvasKivyAgg(my_general.plt.gcf())

        self.gridlayout.add_widget(self.current_graph)


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


class Investment_analysis(App):

    def build(self):
        sm = ScreenManager()

        print("GET DATA ____________________________________\n")
        print("________ PUT MONEY __________________________\n")

        # Download list of operations from backup file
        list_money_movement = my_general.read_data_json(root_path + '\\data\\', 'money_movement')

        # Update list of operations
        my_portfolio.copy_money_operations(my_core.Money(list_money_movement))

        my_portfolio.print_market()

        # my_portfolio.curr_money.deposit_funds(16000.0)  # set money to portfolio : TRUE
        # my_portfolio.curr_money.withdraw_funds(16000.5)  # get money from portfolio : TRUE
        #
        # my_portfolio.curr_money.withdraw_funds(16000000)  # CHECK : FALSE
        # my_portfolio.curr_money.withdraw_funds(0)  # CHECK : FALSE
        # my_portfolio.curr_money.withdraw_funds(0.000001)  # CHECK : FALSE
        # my_portfolio.curr_money.withdraw_funds(0.1)  # CHECK : TRUE
        # my_portfolio.curr_money.withdraw_funds(0.01)  # CHECK : TRUE
        # my_portfolio.curr_money.withdraw_funds(0.9)  # CHECK : TRUE
        # my_portfolio.curr_money.withdraw_funds(0.99)  # CHECK : TRUE
        # my_portfolio.curr_money.withdraw_funds(0.991)  # CHECK : FALSE
        # my_portfolio.curr_money.withdraw_funds(-0.91)  # CHECK : FALSE
        # my_portfolio.curr_money.withdraw_funds(-0.0001)  # CHECK : FALSE
        #
        # # my_portfolio.curr_money.withdraw_all_funds()  # CHECK : TRUE
        # my_portfolio.curr_money.withdraw_funds(15998.0)  # CHECK : TRUE
        # # my_portfolio.curr_money.withdraw_all_funds_plus_taxes(self):  # out all + taxes (13%) TODO (4)
        #
        # print("\n_______________________________________________________________________________________________________\n")
        #
        # my_portfolio.curr_money.deposit_funds(20000.0)  # CHECK : TRUE
        # my_portfolio.curr_money.deposit_funds(0.0)  # CHECK : FALSE
        # my_portfolio.curr_money.deposit_funds(0.000001)  # CHECK : FALSE
        # my_portfolio.curr_money.deposit_funds(0.1)  # CHECK : TRUE)
        # my_portfolio.curr_money.deposit_funds(0.01)  # CHECK : TRUE
        # my_portfolio.curr_money.deposit_funds(0.9)  # CHECK : TRUE
        # my_portfolio.curr_money.deposit_funds(0.99)  # CHECK : TRUE
        # my_portfolio.curr_money.deposit_funds(0.991)  # CHECK : FALSE
        # my_portfolio.curr_money.deposit_funds(-0.9)  # CHECK : FALSE
        #
        # print("\n____________________________________ BUY ____________________________________\n")
        #
        # name_ticker = ['CHMF']
        # depart_market = 'STCK'
        # my_general.name_tickers = name_ticker
        # my_general.depart_market = depart_market
        #
        # # Launch of script which parse MOEX
        # my_general.exec_full(path_name_parser_stocks)
        #
        # # Get info of ticker in the moment
        # list_cur_val = my_general.read_data_json(root_path + '\\data\\', 'market')
        #
        # # Pseudo converting list to object
        # info_ticker = {
        #     "ticker_value": list_cur_val[0][0]["ticker_value"],
        #     "date_value": list_cur_val[0][0]["date_value"],
        #     "time_value": list_cur_val[0][0]["time_value"],
        #     "last_value": list_cur_val[0][0]["last_value"]
        # }
        #
        # print("Current bid : ", info_ticker)
        #
        # count_actives = 1
        #
        # bid = Bid('B', 'CHMF', info_ticker["last_value"], count_actives, 'STCK')
        # my_portfolio.buy(bid)
        #
        # # print("Current cost assets --------> ", my_portfolio.current_profit_ticker(name_ticker, depart_market))
        # # print("Current cost assets percent --------> ", my_portfolio.current_profit_ticker_percent(name_ticker, depart_market))
        # # print("Current cost all assets --------> ", my_portfolio.cost_all_assets())
        # # print("Share assets portfolio percent --------> ", my_portfolio.share_assets_portfolio_percent())
        # # print("Current profit all --------> ", my_portfolio.current_profit_all())
        # # print("Current profit all to percent --------> ", my_portfolio.current_profit_all_percent())
        # # print("Print list current assets --------> ", my_portfolio.print_list_current_assets())
        # # print("Print market --------> ", my_portfolio.print_market(depart_market))
        #
        # start_moment = my_general.datetime.date(2019,
        #                                         1,
        #                                         1)
        # end_moment = my_general.datetime.date(my_general.datetime.datetime.now().year,
        #                                       my_general.datetime.datetime.now().month,
        #                                       my_general.datetime.datetime.now().day)
        #
        # print("Print graph --------> ", my_portfolio.print_graph(list_name_tickers=['CHMF', 'TATN', 'NVTK'],
        #                                                          depart_market=depart_market,
        #                                                          list_name_indicators=['MACD', 'RSI', 'ATR', 'EMA'],
        #                                                          user_start_moment=start_moment,
        #                                                          user_end_moment=end_moment,
        #                                                          user_time_frame='DAILY'))

        # bid = Bid('S', name_ticker, info_ticker["last_value"], count_actives, depart_market)
        # my_portfolio.sell(bid)

        # time_holding = (time_price_in.mounth - time_price_out.mounth); # before sell TODO (1)
        #
        #
        #
        #
        #
        #
        #
        #
        #
        # # Properties of STRATEGY
        # coef_profit = 1.4;
        # ref_profit = (price_in + current_com_broker + current_com_stock_inchange + current_com_found) * (100 + (coef_profit * time_holding)) * 0.01;
        #
        #
        #

        sm.add_widget(PasswordScreen(name='PasswordScreen'))
        sm.add_widget(MainScreen(name='MainScreen'))
        sm.add_widget(DoublerScreen(name='DoublerScreen'))

        return sm


if __name__ == '__main__':
    Investment_analysis().run()
