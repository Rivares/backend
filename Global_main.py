# coding: UTF-8

import lib_general as my_general

my_general.root_path = my_general.path_1 if(my_general.os.path.isdir(my_general.path_1)) else my_general.path_2
root_path = my_general.root_path

path_name_ta_stocks = 'TA_stocks\\TA_stocks.py'
path_name_parser_stocks = 'Parser_market\\Parser_market.py'
market = []

# Properties of BROKER and STOCK EXCHANGE
com_broker = 0.4 * 2  # BUY and SELL
com_stock_exchange = 0.1 * 2


class Money:

    # Precision 2 decimal places
    in_money = {"big_part": 0, "low_part": 0}
    out_money = {"big_part": 0, "low_part": 0}
    current_money = {"big_part": 0, "low_part": 0}
    profit_money = {"big_part": 0, "low_part": 0}
    profit_percent = 0
    result_act = 0  # 2 - success; 1 - cancel; 0 - i.c.; -1 - error;

    def __init__(self, list_params=[]):

        if len(list_params) > 0:
            for param in list_params[-1]:
                self.in_money = param["in_money"]
                self.out_money = param["out_money"]
                self.profit_money = param["profit_money"]
                self.profit_percent = param["profit_percent"]
                self.result_act = param["result_act"]
        else:   # default values
            self.in_money = {"big_part": 0, "low_part": 0}
            self.out_money = {"big_part": 0, "low_part": 0}
            self.current_money = {"big_part": 0, "low_part": 0}
            self.profit_money = {"big_part": 0, "low_part": 0}
            self.profit_percent = 0
            self.result_act = 0  # 2 - success; 1 - cancel; 0 - i.c.; -1 - error;

    def deposit_funds(self, money):     # in

        print("______________ deposit_funds() ______________")
        self.result_act = 1

        in_money = {"big_part": int(money // 1), "low_part": (money % 1)}
        print("in_money[\"low_part\"]  : ", in_money["low_part"] )

        if ((in_money["low_part"] > 0.99) or (in_money["low_part"] < 0.01)) and (in_money["low_part"] != 0.0):    # Precision limit
            self.result_act = -1
        else:
            sum_low_part = self.in_money["low_part"] + in_money["low_part"]

            if (in_money["big_part"] < 0) or (in_money["low_part"] < 0) or (in_money["big_part"] + in_money["low_part"] == 0):
                self.result_act = -1
            else:
                self.in_money["big_part"] += in_money["big_part"]

                if sum_low_part < 60:
                    self.in_money["low_part"] = sum_low_part
                else:
                    self.in_money["big_part"] += 1
                    self.in_money["low_part"] = sum_low_part % 60

                self.current_money["big_part"] += self.in_money["big_part"]
                self.current_money["low_part"] += self.in_money["low_part"]

        print("Operation failed. Error : result_act = ", self.result_act) if (self.result_act < 0) else print(
            "Operation completed successfully.")
        self.result_act = 0

        print("Income : ", self.in_money["big_part"], self.in_money["low_part"])
        print("Outcome : ", self.out_money["big_part"], self.out_money["low_part"])
        print("Current money : ", self.current_money["big_part"], self.current_money["low_part"])

    def withdraw_funds(self, money):    # out

        print("______________ withdraw_funds() ______________")
        self.result_act = 1

        out_money = {"big_part": int(money // 1), "low_part": (money % 1)}
        print("out_money : ", out_money)

        if (out_money["low_part"] > 0.99) or (out_money["low_part"] < 0.01):    # Precision limit
            self.result_act = -1
        else:
            deduction_big = self.current_money["big_part"] - out_money["big_part"]
            deduction_low = self.current_money["low_part"] - out_money["low_part"]

            print("deduction_big : ", deduction_big)
            print("deduction_low : ", deduction_low)

            if (deduction_big < 0) or (out_money["big_part"] < 0) or (out_money["big_part"] + out_money["low_part"] == 0):
                self.result_act = -1
            else:
                if deduction_low >= 0:
                    self.current_money["low_part"] = deduction_low

                    if deduction_big >= 0:
                        self.current_money["big_part"] = deduction_big
                    else:
                        self.result_act = -1
                else:
                    if (self.current_money["big_part"] - 1) >= 0:
                        self.current_money["big_part"] = deduction_big - 1
                        self.current_money["low_part"] = (10 + (10 * abs(self.current_money["low_part"])) - (10 * abs(out_money["low_part"]))) / 10
                    else:
                        self.result_act = -1

                self.out_money["big_part"] += out_money["big_part"]
                self.out_money["low_part"] += out_money["low_part"]

        print("Operation failed. Error : result_act = ", self.result_act) if (self.result_act < 0) else print(
            "Operation completed successfully.")
        self.result_act = 0

        print("Income : ", self.in_money["big_part"], self.in_money["low_part"])
        print("Outcome : ", self.out_money["big_part"], self.out_money["low_part"])
        print("Current money : ", self.current_money["big_part"], self.current_money["low_part"])


class Active:

    ticker = ''
    price = 0.0
    count = 0
    market = ''
    result_act = 0  # 2 - success; 1 - cancel; 0 - i.c.; -1 - error;

    date = {
        "year": 2020,  # default values
        "month": 10,
        "day": 13
    }
    time = {
        "hour": 0,
        "minute": 0,
        "second": 0
    }

    def __init__(self, ticker='', price=0.0, count=0, market=''):

        if (ticker != '') and (price > 0.0) and (count > 0) and (market != ''):
            price = price if (price > 0.0) else 0.0

            count = count if (count >= 1) else 0

            self.market = market

            if (price == 0.0) or (count == 0):
                self.result_act = -1
                print("__________________>>>>> Incorrect bid!")
            else:
                self.ticker = ticker
                self.price = price
                self.count = count
                self.date = {
                    "year": my_general.datetime.datetime.today().strftime("%Y"),
                    "month": my_general.datetime.datetime.today().strftime("%m"),
                    "day": my_general.datetime.datetime.today().strftime("%d")
                }
                self.time = {
                    "hour": my_general.datetime.datetime.today().strftime("%H"),
                    "minute": my_general.datetime.datetime.today().strftime("%M"),
                    "second": my_general.datetime.datetime.today().strftime("%S")
                }

                path = 'backend\\'
                filename = 'active'
                data = []
                data.append({"ticker": self.ticker,
                             "price": self.price,
                             "count": self.count,
                             "market": self.market,
                             "date": self.date,
                             "time": self.time})
                my_general.write_data_json(data, root_path + path, filename)
        else:   # default values
            self.ticker = ''
            self.price = 0.0
            self.count = 0
            self.market = ''
            self.result_act = 0  # 2 - success; 1 - cancel; 0 - i.c.; -1 - error;

            self.date = {
                "year": 2020,  # default values
                "month": 10,
                "day": 13
            }
            self.time = {
                "hour": 0,
                "minute": 0,
                "second": 0
            }

    def clear_bid(self):

        self.ticker = ''
        self.price = 0.0
        self.count = 0
        self.market = ''
        self.date = {
            "year": 2020,  # default values
            "month": 10,
            "day": 13
        }
        self.time = {
            "hour": 0,
            "minute": 0,
            "second": 0
        }


class Portfolio:

    curr_money = Money()
    curr_assetes = []

    def __init__(self):
        self.curr_money = Money()
        self.curr_assetes = []

    def copy_money_operations(self, curr_money_operations):
        self.curr_money = curr_money_operations

    def buy(self, bid):

        require_money = (bid.price * bid.count) + com_broker + com_stock_exchange
        all_money = self.curr_money.current_money["big_part"] + self.curr_money.current_money["low_part"]

        if require_money > all_money:
            print("__________ >>> There is little money in the brokerage account for this operation. Bid was canceled.")
            bid.clear_bid()
        else:
            self.curr_money.withdraw_funds(require_money)  # get money from portfolio
            self.curr_assetes.append(bid)

    def sell(self, bid):    # <<<<< ________________________TODO

        require_assete = (bid.price * bid.count) + com_broker + com_stock_exchange
        # all_money = self.curr_money.current_money["big_part"] + self.curr_money.current_money["low_part"]
        #
        # if require_money > all_money:
        #     print("__________ >>> There is little money in the brokerage account for this operation. Bid was canceled.")
        #     bid.clear_bid()
        # else:
        #     self.curr_money.withdraw_funds(com_broker + com_stock_exchange)  # get money from portfolio
        #     self.curr_assetes.append(bid)

    # def count_assetes(self):
    #
    #
    # def count_assetes(self, ticker):
    #
    #
    # def cost_assetes(self):


def main():

    # Empty portfolio
    my_portfolio = Portfolio()

    list_assetes = []

    print("____________________________________ PUT MONEY ____________________________________\n")

    # Download list of operations from backup file
    list_operations = my_general.read_data_json(root_path + 'backend\\', 'operations')

    # Update list of operations
    my_portfolio.copy_money_operations(Money(list_operations))

    my_portfolio.curr_money.deposit_funds(16000.0)      # set money to portfolio : TRUE
    my_portfolio.curr_money.withdraw_funds(16000.5)     # get money from portfolio : TRUE

    my_portfolio.curr_money.withdraw_funds(16000000)    # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(0)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(0.000001)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(0.9)  # CHECK : TRUE
    my_portfolio.curr_money.withdraw_funds(0.99)  # CHECK : TRUE
    my_portfolio.curr_money.withdraw_funds(0.991)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(-0.91)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(-0.0001)  # CHECK : FALSE

    my_portfolio.curr_money.withdraw_funds(97.710)  # set money to portfolio : TRUE ( must 0): TODO
    my_portfolio.curr_money.deposit_funds(20000.0)  # set money to portfolio : TRUE ( must 20000) TODO

    print("____________________________________ BUY ____________________________________\n")

    name_ticker = 'MAIL'
    depart_market = 'STCK'
    my_general.name_ticker = name_ticker
    my_general.depart_market = depart_market

    # Launch of script which parse MOEX
    my_general.exec_full(path_name_parser_stocks)

    # Get info of ticker in the moment
    list_cur_val = my_general.read_data_json(root_path + 'backend\\Parser_market\\', 'market')

    # Pseudo converting list to object
    info_ticker = {
        "ticker_value": list_cur_val[0][0]["ticker_value"],
        "date_value": list_cur_val[0][0]["date_value"],
        "time_value": list_cur_val[0][0]["time_value"],
        "last_value": list_cur_val[0][0]["last_value"]
    }

    print("Current bid : ", info_ticker)

    count_actives = 1
    bid = Active(name_ticker, info_ticker["last_value"], count_actives, depart_market)

    # Validation bid !!! (date, time) – 10:40 – 23:30 -> true; otherwise -> false; <<<<< ________________________TODO

    my_portfolio.buy(bid)

    my_portfolio.sell(bid)








    # time_holding = (time_price_in.mounth - time_price_out.mounth);
    # com_found = * 2;
    # current_com_broker = (price_out - price_in) * com_broker;
    # current_com_stock_inchange = (price_out - price_in) * com_stock_exchange;
    # current_com_found = (price_out - price_in) * com_found;
    # current_profit = (price_out - price_in - current_com_broker - current_com_stock_inchange - current_com_found)
    #
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

    # while (my_general.datetime.datetime.now().hour > 9) and (my_general.datetime.datetime.now().hour < 23):
    #
    #     path = 'Helper\\TA_stocks\\'
    #     filename = 'result_ta'
    #     result_ta = my_general.read_data_json(root_path + path, filename)
    #
    #     path = 'Helper\\Parser_market\\'
    #     filename = 'market'
    #     market = my_general.read_data_json(root_path + path, filename)
    #
    #     # print(prediction_e_n)
    #     # print(prediction_p_n)
    #     # print(market)
    #     # print(result_ta)
    #
    #     print("__________________ Global training __________________")
    #
    #     my_general.np.random.seed(2)
    #     path = 'Helper\\'
    #     model_name = root_path + path + 'NN_Main_model.h5'
    #
    #     X = []
    #     Y = []
    #
    #     Y.append(result_ta[0]['diff_value'])
    #
    #     X.append(prediction_e_n['score'])
    #
    #     X.append(prediction_p_n['score'])
    #
    #     for ticker in market:
    #         for input in ticker:
    #             X.append(input['open_value'])
    #             X.append(input['close_value'])
    #             X.append(input['high_value'])
    #             X.append(input['low_value'])
    #             X.append(input['volume_value'])
    #
    #     X.append(result_ta[0]['open_value'])
    #     X.append(result_ta[0]['close_value'])
    #     X.append(result_ta[0]['high_value'])
    #     X.append(result_ta[0]['low_value'])
    #     X.append(result_ta[0]['volume_value'])
    #     X.append(result_ta[0]['adi_i'])
    #     X.append(result_ta[0]['adx_aver'])
    #     X.append(result_ta[0]['adx_DI_pos'])
    #     X.append(result_ta[0]['adx_DI_neg'])
    #     X.append(result_ta[0]['ai_i'])
    #     X.append(result_ta[0]['ai_up'])
    #     X.append(result_ta[0]['ai_down'])
    #     X.append(result_ta[0]['ao_i'])
    #     X.append(result_ta[0]['atr_i'])
    #     X.append(result_ta[0]['bb_bbh'])
    #     X.append(result_ta[0]['bb_bbl'])
    #     X.append(result_ta[0]['bb_bbm'])
    #     X.append(result_ta[0]['ccl_i'])
    #     X.append(result_ta[0]['cmf_i'])
    #     X.append(result_ta[0]['cmf_signal'])
    #     X.append(result_ta[0]['cr_i'])
    #
    #     X.append(result_ta[0]['dc_dch'])
    #     X.append(result_ta[0]['dc_dcl'])
    #     X.append(result_ta[0]['dlr_i'])
    #     X.append(result_ta[0]['dpo_i'])
    #     X.append(result_ta[0]['ema_i'])
    #     X.append(result_ta[0]['fi_i'])
    #     X.append(result_ta[0]['ichimoku_a'])
    #     X.append(result_ta[0]['ichimoku_b'])
    #     X.append(result_ta[0]['kama_i'])
    #     X.append(result_ta[0]['kc_kcc'])
    #     X.append(result_ta[0]['kc_kch'])
    #     X.append(result_ta[0]['kc_kcl'])
    #     X.append(result_ta[0]['kst'])
    #     X.append(result_ta[0]['kst_diff'])
    #     X.append(result_ta[0]['kst_sig'])
    #     X.append(result_ta[0]['vi_diff'])
    #     X.append(result_ta[0]['vi_neg'])
    #     X.append(result_ta[0]['vi_pos'])
    #
    #     X.append(result_ta[0]['mfi_i'])
    #     X.append(result_ta[0]['mi'])
    #     X.append(result_ta[0]['nvi_i'])
    #     X.append(result_ta[0]['obv_i'])
    #     X.append(result_ta[0]['psar_i'])
    #     X.append(result_ta[0]['psar_up'])
    #     X.append(result_ta[0]['psar_down'])
    #     X.append(result_ta[0]['roc_i'])
    #     X.append(result_ta[0]['rsi_i'])
    #     X.append(result_ta[0]['stoch_i'])
    #     X.append(result_ta[0]['stoch_signal'])
    #     X.append(result_ta[0]['trix_i'])
    #     X.append(result_ta[0]['tsi_i'])
    #     X.append(result_ta[0]['uo_i'])
    #     X.append(result_ta[0]['vpt_i'])
    #
    #     count_inputs = len(X)
    #     print("Len NN: " + str(count_inputs))
    #     print("X: "); print(X)
    #     print("Y: "); print(Y)
    #
    # else:
    #     print("Sleep...")


if __name__ == '__main__':
    main()
