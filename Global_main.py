# coding: UTF-8

import lib_general as my_general
import lib_gui as my_gui
import lib_core as my_core

root_path = my_general.root_path

def main():

    # Empty portfolio
    my_portfolio = my_core.Portfolio()

    print("GET DATA ____________________________________\n")
    print("________ PUT MONEY __________________________\n")

    # Download list of operations from backup file
    list_money_movement = my_general.read_data_json(root_path + '\\data\\', 'money_movement')

    # Update list of operations
    my_portfolio.copy_money_operations(my_core.Money(list_money_movement))

    my_portfolio.print_market()
    gui = my_gui.Investment_analysis()
    gui.run()

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


if __name__ == '__main__':
    main()
