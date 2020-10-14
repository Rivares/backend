# coding: UTF-8

import lib_general as my_general

my_general.root_path = 'C:\\Users\\user\\0_Py\\'
root_path = 'C:\\Users\\User\\0_Py\\'

path_name_ta_stocks = 'TA_stocks\\TA_stocks.py'
path_name_parser_stocks = 'Parser_market/Parser_market.py'
market = []

# Properties of BROKER and STOCK EXCHANGE
com_broker = 0.4 * 2  # BUY and SELL
com_stock_exchange = 0.1 * 2  # __________________________________________________________________________________!!!!!


class money:
    in_money = {"big_part": 0, "low_part": 0}
    out_money = {"big_part": 0, "low_part": 0}
    profit_money = {"big_part": 0, "low_part": 0}
    profit_percent = 0
    result_act = 0  # 2 - success; 1 - cancel; 0 - i.c.; -1 - error;

    def __init__(self, list_params):
        for param in list_params[-1]:
            self.in_money = param["in_money"]
            self.out_money = param["out_money"]
            self.profit_money = param["profit_money"]
            self.profit_percent = param["profit_percent"]
            self.result_act = param["result_act"]

    def deposit_funds(self, money): # in
        in_money = {"big_part": int(money // 1), "low_part": (money % 1)}

        self.in_money["big_part"] += in_money["big_part"]

        sum_low_part = self.in_money["low_part"] + in_money["low_part"]

        if sum_low_part < 60:
            self.in_money["low_part"] = sum_low_part
        else:
            self.in_money["big_part"] += 1
            self.in_money["low_part"] = sum_low_part % 60

    def withdraw_funds(self, money): # out
        out_money = {"big_part": int(money // 1), "low_part": (money % 1)}

        deduction_big = self.in_money["big_part"] - out_money["big_part"]
        deduction_low = self.in_money["low_part"] - out_money["low_part"]
        # __________________________________________________________________________________!!!!!
        print(deduction_big)
        print(deduction_low)

        if deduction_big >= 0:
            self.out_money["big_part"] = deduction_big
        else:
            self.result_act = -1

        if deduction_low >= 0:
            self.out_money["low_part"] = deduction_low
        else:
            self.out_money["big_part"] -= 1
            self.out_money["low_part"] = 10 - abs(deduction_low)


class active:
    ticker = ''
    price = 0.0
    count = 0
    act = ""
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

    def __init__(self, ticker, price, count, act):

        price = price if (price > 0.0) else 0.0

        count = count if (count >= 1) else 0

        act = act if ((act == "buy") or (act == "sell")) else ""

        if (price == 0.0) or (count == 0) or (act == ""):
            self.result_act = -1
            print("__________________>>>>> Incorrect bid!")
        else:
            self.ticker = ticker
            self.price = price
            self.count = count
            self.act = act
            self.date = {
                "year": my_general.datetime.date.year,
                "month": my_general.datetime.date.month,
                "day": my_general.datetime.date.day
            }
            self.time = {
                "hour": my_general.datetime.time.hour,
                "minute": my_general.datetime.time.minute,
                "second": my_general.datetime.time.second
            }


def main():
    print("__________________ PUT MONEY __________________")

    path = 'backend\\'
    filename = 'money'
    list_investments = my_general.read_data_json(root_path + path, filename)

    current_invest = money(list_investments)

    print(current_invest.in_money)
    print(current_invest.out_money)
    print(current_invest.profit_money)
    print(current_invest.profit_percent)
    print(current_invest.result_act)

    current_invest.deposit_funds(16000.0)

    print("Income : "); print(current_invest.in_money)
    print("Outcome : "); print(current_invest.out_money)

    current_invest.withdraw_funds(16000.0)

    print("Income : "); print(current_invest.in_money)
    print("Outcome : "); print(current_invest.out_money)



    print("__________________ BUY __________________")

    name_ticker = 'ETLN'
    depart_market = 'STCK'  # GDS: Goods; CRNCY: Currency; INDXS_WR: Indexes(W+R); INDXS_WU: Indexes(W+U); STCK: Stock
    my_general.name_ticker = name_ticker
    my_general.depart_market = depart_market

    my_general.exec_full(path_name_parser_stocks)

    path = 'backend\\Parser_market\\'
    filename = 'market'
    list_cur_val = my_general.read_data_json(root_path + path, filename)

    for it in list_cur_val:
        current_price = {
            "ticker_value": it[0]["ticker_value"],
            "date_value": it[0]["date_value"],
            "time_value": it[0]["time_value"],
            "last_value": it[0]["last_value"]
        }

    print(current_price)

    count_actives = 1
    stock = active(name_ticker, current_price["last_value"], count_actives, "buy")






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
