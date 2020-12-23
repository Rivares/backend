# coding: UTF-8

import lib_general as my_general

root_path = my_general.root_path

path_name_ta_stocks = 'TA_stocks\\TA_stocks.py'
path_name_parser_stocks = 'Parser_market\\Parser_market.py'
market = []

# Properties of BROKER and STOCK EXCHANGE
com_broker = 0.4 * 2  # BUY and SELL
com_stock_exchange = 0.1 * 2


# Properties of STRATEGY
coeff_profit = 1.5  # in month


class Money:
    # Precision 2 decimal places
    in_money = {"big_part": 0, "low_part": 0.0}
    out_money = {"big_part": 0, "low_part": 0.0}
    current_money = {"big_part": 0, "low_part": 0.0}
    profit_money = {"big_part": 0, "low_part": 0.0}
    profit_percent = 0.0
    result_act = 0  # 2 - success; 1 - cancel; 0 - i.c.; -1 - error;

    def __init__(self, list_params=None):

        if list_params is None:
            list_params = []
        if len(list_params) > 0:
            for param in list_params:
                print("param : ", param)
                self.in_money = param["in_money"]
                self.out_money = param["out_money"]
                self.profit_money = param["profit_money"]
                self.profit_percent = param["profit_percent"]
                self.result_act = param["result_act"]
        else:  # default values
            self.in_money = {"big_part": 0, "low_part": 0.0}
            self.out_money = {"big_part": 0, "low_part": 0.0}
            self.current_money = {"big_part": 0, "low_part": 0.0}
            self.profit_money = {"big_part": 0, "low_part": 0.0}
            self.profit_percent = 0.0
            self.result_act = 0  # 2 - success; 1 - cancel; 0 - i.c.; -1 - error;

    def deposit_funds(self, money):  # in

        print("\n______________ deposit_funds() ______________\n")
        self.result_act = 1

        in_money = {"big_part": int(money // 1), "low_part": (money % 1)}
        print("in_money  : ", in_money)

        # Precision limit

        if ((in_money["low_part"] > 0.99) or (in_money["low_part"] < 0.01)) and (in_money["low_part"] != 0.0):
            self.result_act = -1
        else:
            sum_low_part = round(self.current_money["low_part"] + in_money["low_part"], 2)
            print("sum_low_part  : ", sum_low_part)

            if (in_money["big_part"] < 0) or (in_money["low_part"] < 0) or \
                    (in_money["big_part"] + in_money["low_part"] == 0):
                self.result_act = -1
            else:
                self.in_money["big_part"] += in_money["big_part"]
                self.current_money["big_part"] += in_money["big_part"]

                if sum_low_part < 1.0:
                    self.in_money["low_part"] = sum_low_part

                    self.current_money["low_part"] = sum_low_part
                else:
                    self.in_money["big_part"] += 1
                    self.in_money["low_part"] = round(sum_low_part - 1, 2)

                    self.current_money["big_part"] += 1
                    self.current_money["low_part"] = self.in_money["low_part"]

        path = '\\data\\'
        filename = 'money_movement'

        new_data = my_general.read_data_json(root_path + path, filename)
        new_data.append({
            "in_money": {"big_part": self.in_money["big_part"], "low_part": self.in_money["low_part"]},
            "out_money": {"big_part": self.out_money["big_part"], "low_part": self.out_money["low_part"]},
            "current_money": {"big_part": self.current_money["big_part"], "low_part": self.current_money["low_part"]},
            "profit_money": {"big_part": self.profit_money["big_part"], "low_part": self.profit_money["low_part"]},
            "profit_percent": self.profit_percent,
            "result_act": self.result_act
        })

        my_general.write_data_json(new_data, root_path + path, filename)

        print("Operation failed. Error : result_act = ", self.result_act) if (self.result_act < 0) else print(
            "Operation completed successfully.")
        self.result_act = 0

        print("Income : ", self.in_money["big_part"], self.in_money["low_part"])
        print("Outcome : ", self.out_money["big_part"], self.out_money["low_part"])
        print("Current money : ", self.current_money["big_part"], self.current_money["low_part"])

    def withdraw_funds(self, money):  # out

        print("\n______________ withdraw_funds() ______________\n")
        self.result_act = 1

        out_money = {"big_part": int(money // 1), "low_part": (money % 1)}
        print("out_money : ", out_money)

        if ((out_money["low_part"] > 0.99) or (out_money["low_part"] < 0.01)) and (
                round(out_money["low_part"], 2) != 0.0):  # Precision limit
            self.result_act = -1
        else:
            out_money["low_part"] = round((money % 1), 2)

            deduction_big = self.current_money["big_part"] - out_money["big_part"]
            deduction_low = round(self.current_money["low_part"] - out_money["low_part"], 2)
            sum_low_part = round(self.out_money["low_part"] + out_money["low_part"], 2)

            print("deduction_big : ", deduction_big)
            print("deduction_low : ", deduction_low)

            if (deduction_big < 0) or (out_money["big_part"] < 0) or \
                    (out_money["big_part"] + out_money["low_part"] == 0) or \
                    ((self.current_money["big_part"] + self.current_money["low_part"] - (
                            out_money["big_part"] + out_money["low_part"])) < 0):
                self.result_act = -1
            else:
                if deduction_low >= 0:
                    self.current_money["low_part"] = deduction_low

                    if sum_low_part >= 1.0:
                        self.out_money["big_part"] += 1
                        self.out_money["low_part"] = round(sum_low_part - 1, 2)
                    else:
                        self.out_money["low_part"] += round(out_money["low_part"], 2)

                    if deduction_big >= 0:
                        self.current_money["big_part"] = deduction_big

                        self.out_money["big_part"] += out_money["big_part"]
                    else:
                        self.result_act = -1
                else:
                    if (self.current_money["big_part"] - 1) >= 0:
                        self.current_money["big_part"] = deduction_big - 1
                        self.current_money["low_part"] = round(((10 + (10 * abs(self.current_money["low_part"])) - (
                                    10 * abs(out_money["low_part"]))) / 10), 2)

                        if sum_low_part >= 1.0:
                            self.out_money["big_part"] += 1
                            self.out_money["low_part"] = round(sum_low_part - 1, 2)
                        else:
                            self.out_money["big_part"] += out_money["big_part"]
                            self.out_money["low_part"] += round(out_money["low_part"], 2)
                    else:
                        self.result_act = -1

        path = '\\data\\'
        filename = 'money_movement'

        new_data = my_general.read_data_json(root_path + path, filename)
        new_data.append({
            "in_money": {"big_part": self.in_money["big_part"], "low_part": self.in_money["low_part"]},
            "out_money": {"big_part": self.out_money["big_part"], "low_part": self.out_money["low_part"]},
            "current_money": {"big_part": self.current_money["big_part"], "low_part": self.current_money["low_part"]},
            "profit_money": {"big_part": self.profit_money["big_part"], "low_part": self.profit_money["low_part"]},
            "profit_percent": self.profit_percent,
            "result_act": self.result_act
        })

        my_general.write_data_json(new_data, root_path + path, filename)

        print("Operation failed. Error : result_act = ", self.result_act) if (self.result_act < 0) else print(
            "Operation completed successfully.")
        self.result_act = 0

        print("Income : ", self.in_money["big_part"], self.in_money["low_part"])
        print("Outcome : ", self.out_money["big_part"], self.out_money["low_part"])
        print("Current money : ", self.current_money["big_part"], self.current_money["low_part"])

    def withdraw_all_funds(self):  # out all

        print("\n______________ withdraw_all_funds() ______________\n")

        self.out_money["big_part"] += self.current_money["big_part"]
        self.out_money["low_part"] += round(self.current_money["low_part"], 2)

        self.current_money["big_part"] = 0
        self.current_money["low_part"] = 0.0

        print("Income : ", self.in_money["big_part"], self.in_money["low_part"])
        print("Outcome : ", self.out_money["big_part"], self.out_money["low_part"])
        print("Current money : ", self.current_money["big_part"], self.current_money["low_part"])

    def withdraw_all_funds_plus_taxes(self):  # out all + taxes (13%) TODO (4)

        print("\n______________ withdraw_all_funds_plus_taxes() ______________\n")

        self.out_money["big_part"] += self.current_money["big_part"]
        self.out_money["low_part"] += round(self.current_money["low_part"], 2)

        self.current_money["big_part"] = 0
        self.current_money["low_part"] = 0.0

        print("Income : ", self.in_money["big_part"], self.in_money["low_part"])
        print("Outcome : ", self.out_money["big_part"], self.out_money["low_part"])
        print("Current money : ", self.current_money["big_part"], self.current_money["low_part"])


class Bid:
    act = ''
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

    def __init__(self, act, ticker='', price=0.0, count=0, market=''):

        curr_date_d = my_general.datetime.datetime.today().isoweekday()
        curr_time_h = my_general.datetime.datetime.today().strftime("%H")

        # int(curr_time_h) < 10) TODO (!)
        if (ticker != '') and (price > 0.0) and (count > 0) and (market != '') and \
           (int(curr_time_h) > 10) and (int(curr_time_h) < 24) and (curr_date_d != 6) and (curr_date_d != 7):

            price = price if (price > 0.0) else 0.0

            count = count if (count >= 1) else 0

            self.act = act if ((act == 'B') or (act == 'S')) else ''

            self.market = market

            if (price == 0.0) or (count == 0):
                self.result_act = -1
                print("__________________>>>>> Incorrect bid!")
            else:
                self.ticker = ticker
                self.price = price
                self.count = count
                self.result_act = 0
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

        else:  # default values
            self.act = ''
            self.ticker = ''
            self.price = 0.0
            self.count = 0
            self.market = ''
            self.result_act = -1  # 2 - success; 1 - cancel; 0 - i.c.; -1 - error;

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
            print("__________________>>>>> Incorrect bid!")

    def clear_bid(self):
        self.act = ''
        self.ticker = ''
        self.price = 0.0
        self.count = 0
        self.market = ''
        self.result_act = 0
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
    curr_assets = []
    count_all_assets = 0

    def __init__(self):
        self.curr_money = Money()
        self.curr_assets = []
        self.count_all_assets = 0

    # Load current money
    def copy_money_operations(self, curr_money_operations):
        self.curr_money = curr_money_operations

    # Load assets from file
    def copy_current_data_of_assets(self):

        print("\n______________ copy_current_data_of_assets() ______________\n")

        path = '\\data\\'
        filename = 'list_current_assets'

        curr_assets = my_general.read_data_json(root_path + path, filename)
        self.curr_assets.clear()

        for it in curr_assets:
            if it["act"] == "B":
                self.curr_assets.append({"id": it["id"],
                                         "act": it["act"],
                                         "ticker": it["ticker"],
                                         "price": it["price"],
                                         "count": it["count"],
                                         "cost": it["cost"],
                                         "commissions": it["commissions"],
                                         "full_cost": it["full_cost"],
                                         "market": it["market"],
                                         "date": it["date"],
                                         "time": it["time"]})

    def buy(self, bid):

        print("\n______________ buy() ______________\n")

        if bid.result_act == -1:
            print("__________________>>>>> Incorrect bid! : bid.result_act = ", bid.result_act)
            return

        cost = bid.price * bid.count
        commissions = round((((cost * com_broker) + (cost * com_stock_exchange)) * 0.01), 2)
        require_money = round(cost + commissions, 2)

        print("Price : ", bid.price)
        print("Count : ", bid.count)
        print("Cost : ", cost)
        print("Commissions : ", commissions)
        print("Require money : ", require_money)

        all_money = round(self.curr_money.current_money["big_part"] + self.curr_money.current_money["low_part"], 2)

        if require_money > all_money:
            print("__________ >>> There is little money in the brokerage account for this operation. Bid was canceled.")
            bid.clear_bid()
        else:

            # connect to API Tinkoff Invest TODO (3)

            status_bid = True  # Answer from API Tinkoff Invest

            curr_time = {
                "hour": my_general.datetime.datetime.today().strftime("%H"),
                "minute": my_general.datetime.datetime.today().strftime("%M"),
                "second": my_general.datetime.datetime.today().strftime("%S")
            }
            curr_date = {
                "year": my_general.datetime.datetime.today().strftime("%Y"),
                "month": my_general.datetime.datetime.today().strftime("%m"),
                "day": my_general.datetime.datetime.today().strftime("%d")
            }

            if status_bid:

                # BOUGHT

                self.curr_money.withdraw_funds(require_money)  # get money from portfolio

                self.copy_current_data_of_assets()

                self.curr_assets.append({"id": my_general.random.randint(1000000000, 9999999999),
                                         "act": bid.act,
                                         "ticker": bid.ticker,
                                         "price": bid.price,
                                         "count": bid.count,
                                         "cost": cost,
                                         "commissions": commissions,
                                         "full_cost": require_money,
                                         "market": bid.market,
                                         "date": curr_date,
                                         "time": curr_time})

                path = '\\data\\'
                filename = 'list_current_assets'

                print("__________ >>> Bid executed.")
                my_general.write_data_json(self.curr_assets, root_path + path, filename)

                filename = 'list_operations_assets'
                my_general.write_data_json(self.curr_assets, root_path + path, filename)
            else:
                print("__________ >>> Bid not executed.")

    def sell(self, bid):

        print("\n______________ sell() ______________\n")

        if bid.result_act == -1:
            print("__________________>>>>> Incorrect bid! : bid.result_act = ", bid.result_act)
            return

        cost = bid.price * bid.count
        commissions = round((((cost * com_broker) + (cost * com_stock_exchange)) * 0.01), 2)
        get_money = round(cost - commissions, 2)

        print("Price : ", bid.price)
        print("Count : ", bid.count)
        print("Cost : ", cost)
        print("Commissions : ", commissions)
        print("Get money : ", get_money)

        average_cost, count_month, my_asset, prev_data = self.average_cost_assets(bid.ticker, bid.count)

        if average_cost == -1:
            print("__________ >>> There is not asset in the brokerage account for this operation. Bid was canceled.")
            bid.clear_bid()
            return
        else:

            # Profit on sale
            profit_money = get_money - average_cost
            percent_profit = profit_money * 100 / average_cost

            print("percent_profit : ", percent_profit)

            if percent_profit < coeff_profit * count_month:     # coeff_profit * count_month = 1.5 * month => 15% / year
                print("Warning!!! Profit more small!!! >>> ", profit_money, " : ", percent_profit, "%")
                # Ask to user ! TODO (4)
            else:
                print("Great deal!!! >>> ", profit_money, " : ", percent_profit, "%")

            # connect to API Tinkoff Invest TODO (3)

            status_bid = True  # Answer from API Tinkoff Invest

            curr_time = {
                "hour": my_general.datetime.datetime.today().strftime("%H"),
                "minute": my_general.datetime.datetime.today().strftime("%M"),
                "second": my_general.datetime.datetime.today().strftime("%S")
            }

            curr_date = {
                "year": my_general.datetime.datetime.today().strftime("%Y"),
                "month": my_general.datetime.datetime.today().strftime("%m"),
                "day": my_general.datetime.datetime.today().strftime("%d")
            }

            if status_bid:

                # SOLD
                self.curr_money.deposit_funds(get_money)

                new_data = prev_data
                new_data.append({"id": my_general.random.randint(1000000000, 9999999999),
                                 "act": bid.act,
                                 "ticker": bid.ticker,
                                 "price": bid.price,
                                 "count": bid.count,
                                 "cost": cost,
                                 "commissions": commissions,
                                 "full_cost": get_money,
                                 "market": bid.market,
                                 "date": curr_date,
                                 "time": curr_time})

                path = '\\data\\'
                filename = 'list_current_assets'

                print("__________ >>> Bid executed.")
                my_general.write_data_json(new_data, root_path + path, filename)

                filename = 'list_operations_assets'
                my_general.write_data_json(new_data, root_path + path, filename)

                # Delete previously purchase

                self.copy_current_data_of_assets()
                new_data = self.curr_assets

                # Get all purchase the ticker
                for it_1 in new_data:
                    for it_2 in my_asset:
                        if it_1["id"] == it_2["id"]:
                            new_data.remove(it_1)
                            self.curr_assets.pop(it_1)

                # Rewrite data without previously purchase
                my_general.write_data_json(new_data, root_path + path, filename)
            else:
                print("__________ >>> Bid not executed.")

    def count_assets(self, ticker=''):

        print("\n______________ count_assets() ______________\n")

        self.copy_current_data_of_assets()
        count_all_assets = 0
        count_ticker = 0
        i = 0

        while i < len(self.curr_assets):
            if ticker != '':
                if self.curr_assets[i]["ticker"] == ticker:
                    count_ticker += 1
            else:
                count_all_assets += 1

            i += 1

        self.count_all_assets = count_all_assets

        return count_ticker

    def count_assets_percent(self, ticker):

        print("\n______________ count_assets_percent() ______________\n")

        self.copy_current_data_of_assets()
        count_ticker = 0

        for it in self.curr_assets:
            if it["ticker"] == ticker:
                count_ticker += 1

        return (count_ticker * 100) / len(self.curr_assets)

    def average_cost_assets(self, name_ticker, count_ticker=1):

        print("\n______________ average_cost_assets() ______________\n")

        my_asset = []
        count_month = 0

        self.copy_current_data_of_assets()
        prev_data = self.curr_assets

        # Get all purchase the ticker
        for it in prev_data:
            if (it["ticker"] == name_ticker) and (int(it["count"]) >= count_ticker):
                data = {
                    "id": int(it["id"]),
                    "full_cost": float(it["full_cost"]),
                    "count": int(it["count"]),
                    "month": int(it["date"]["month"])
                }
                my_asset.append(data)

        if len(my_asset) <= 0:
            print("_______ >>> There is not asset in the brokerage account for this operation. Operation was canceled.")
            return -1, -1, -1, -1
        else:

            # Get count month which hide this ticker
            buff_month = int(my_asset[0]["month"])
            count_month += 1
            for it in my_asset:

                if int(it["month"]) != buff_month:
                    count_month += 1
                    buff_month = int(it["month"])

            # Get average full_cost purchase the ticker
            sum_cost = 0.0
            count = 0
            for it in my_asset:
                sum_cost += it["full_cost"]
                count += 1

            average_cost = float(sum_cost / count)

            return average_cost, count_month, my_asset, prev_data

    def average_commission_ticker(self, name_ticker):

        print("\n______________ average_commission_ticker() ______________\n")

        self.copy_current_data_of_assets()
        sum_commission = 0.0
        count = 0

        # Get all purchase the ticker
        for it in self.curr_assets:
            if (it["ticker"] == name_ticker) and (int(it["count"]) > 0):
                sum_commission += float(it["commissions"])
                count += 1

        average_commission = sum_commission / count

        return average_commission

    def sum_commission_ticker(self, name_ticker):

        print("\n______________ sum_commission_ticker() ______________\n")

        self.copy_current_data_of_assets()
        sum_commission = 0.0

        # Get all purchase the ticker
        for it in self.curr_assets:
            if (it["ticker"] == name_ticker) and (int(it["count"]) > 0):
                sum_commission += float(it["commissions"])

        return sum_commission

    def cost_all_assets(self):

        print("\n______________ cost_all_assets() ______________\n")

        self.copy_current_data_of_assets()  # Update current_list_assets

        all_full_price = 0

        for it in self.curr_assets:
            average_cost, count_month, my_asset, prev_data = self.average_cost_assets(it["ticker"])
            all_full_price += average_cost

        return round(all_full_price, 2)

    def share_assets_portfolio_percent(self):
        self.copy_current_data_of_assets()  # Update current_list_assets

        curr_all_full_price = self.cost_all_assets()
        curr_all_money = self.curr_money.current_money["big_part"] + self.curr_money.current_money["low_part"]

        return round((100.0 - ((curr_all_money * 100) / (curr_all_full_price + curr_all_money))), 2)

    def cost_ticker_assets(self, name_ticker):

        print("\n______________ cost_ticker_assets() ______________\n")

        self.copy_current_data_of_assets()  # Update current_list_assets
        average_cost, count_month, my_asset, prev_data = self.average_cost_assets(name_ticker)

        return average_cost

    def current_profit_ticker(self, name_ticker, depart_market):

        print("\n______________ current_profit_ticker() ______________\n")

        # 1. Get initial_price of ticker from my_assets

        count_assets = self.count_assets(name_ticker)
        initial_average_full_price, count_month, my_asset, prev_data = self.average_cost_assets(name_ticker)
        initial_average_full_price = round(initial_average_full_price * count_assets, 2)

        print("Initial average full price : ", initial_average_full_price)

        if initial_average_full_price > 0:

            # 2. Get current_price of ticker from market

            my_general.name_ticker = name_ticker
            my_general.depart_market = depart_market

            # Launch of script which parse MOEX
            my_general.exec_full(path_name_parser_stocks)

            # Get info of ticker in the moment
            list_cur_val = my_general.read_data_json(root_path + '\\Parser_market\\', 'market')

            # Pseudo converting list to object
            info_ticker = {
                "ticker_value": list_cur_val[0][0]["ticker_value"],
                "date_value": list_cur_val[0][0]["date_value"],
                "time_value": list_cur_val[0][0]["time_value"],
                "last_value": list_cur_val[0][0]["last_value"]
            }

            current_price = float(info_ticker["last_value"])
            print("Current price : ", current_price)

            cost = current_price * count_assets
            commissions = round((((cost * com_broker) + (cost * com_stock_exchange)) * 0.01), 2)
            current_full_price = round(cost - commissions, 2)

            print("Full price (with commissions) : ", current_full_price)

            # 3. Get current_cost_assets of ticker

            current_cost_assets = current_full_price - initial_average_full_price

            return round(current_cost_assets, 2), current_full_price, initial_average_full_price
        else:
            return -1, -1, -1

    def current_profit_ticker_percent(self, name_ticker, depart_market):

        print("\n______________ current_profit_ticker_percent() ______________\n")

        current_cost_assets, current_full_price, initial_average_full_price = \
            self.current_profit_ticker(name_ticker, depart_market)

        return round((((current_full_price * 100) / initial_average_full_price) - 100.0), 2)

    def current_profit_all(self):

        print("\n______________ current_profit_all() ______________\n")

        self.copy_current_data_of_assets()  # Update current_list_assets

        full_profit = 0.0
        prev_ticker = ''

        for it in self.curr_assets:
            if prev_ticker != it["ticker"]:
                current_cost_assets, current_full_price, initial_average_full_price = \
                    self.current_profit_ticker(it["ticker"], it["market"])
                full_profit += current_cost_assets
                prev_ticker = it["ticker"]

        return round(full_profit, 2)

    def current_profit_all_percent(self):

        print("\n______________ current_profit_all_percent() ______________\n")

        full_profit = self.current_profit_all()
        prev_ticker = ''

        initial_average_full_price = 0.0

        for it in self.curr_assets:
            if prev_ticker != it["ticker"]:
                count_assets = self.count_assets(it["ticker"])
                initial_average_full_price_ticker, count_month, my_asset, prev_data = \
                    self.average_cost_assets(it["ticker"])
                initial_average_full_price += round(initial_average_full_price_ticker * count_assets, 2)

                # print("initial_average_full_price_ticker : ", initial_average_full_price_ticker)
                # print("initial_average_full_price : ", initial_average_full_price)

                prev_ticker = it["ticker"]

        return round(((full_profit * 100) / initial_average_full_price), 2)

    def print_list_current_assets(self):

        print("\n______________ print_list_current_assets() ______________\n")

        prev_ticker = ''

        for it in self.curr_assets:
            if prev_ticker != it["ticker"]:
                ticker = it["ticker"]
                aver_price, count_month, my_asset, prev_data = self.average_cost_assets(it["ticker"])
                count = self.count_assets(it["ticker"])
                sum_commissions = self.sum_commission_ticker(it["ticker"])

                prev_ticker = it["ticker"]

                print("Ticker : ", ticker)
                print("Average price : ", aver_price)
                print("Count : ", count)
                print("Sum of commission : ", sum_commissions)

    def print_market(self, depart_market):

        print("\n______________ print_market() ______________\n")

        name_ticker = ''    # All ticker
        my_general.name_ticker = name_ticker
        my_general.depart_market = depart_market

        # Launch of script which parse MOEX
        my_general.exec_full(path_name_parser_stocks)

        # Get info of ticker in the moment
        list_cur_val = my_general.read_data_json(root_path + '\\Parser_market\\', 'market')

        for ticker in list_cur_val:
            print("Ticker : ", ticker["ticker_value"])
            print("Price : ", ticker["last_value"])
            print("Volume : ", ticker["volume_value"])

    def print_graph(self, list_name_tickers, depart_market, list_name_indicators,
                    user_start_moment=my_general.datetime.date(my_general.datetime.datetime.now().year, 1, 1),
                    user_end_moment=my_general.datetime.date(my_general.datetime.datetime.now().year,
                                                             my_general.datetime.datetime.now().month,
                                                             my_general.datetime.datetime.now().day),
                    user_time_frame='HOURLY'):

        print("\n______________ print_graph() ______________\n")

        list_tickers = []

        my_general.name_tickers = list_name_tickers
        my_general.depart_market = depart_market
        my_general.indicators_market = list_name_indicators

        my_general.start_moment = user_start_moment
        my_general.end_moment = user_end_moment
        my_general.time_frame = user_time_frame

        # 1. Get historical data

        const_time_frame = {
            "MINUTES1": my_general.Timeframe.MINUTES1,
            "MINUTES5": my_general.Timeframe.MINUTES5,
            "MINUTES10": my_general.Timeframe.MINUTES10,
            "MINUTES15": my_general.Timeframe.MINUTES15,
            "MINUTES30": my_general.Timeframe.MINUTES30,
            "HOURLY": my_general.Timeframe.HOURLY,
            "DAILY": my_general.Timeframe.DAILY,
            "WEEKLY": my_general.Timeframe.WEEKLY,
            "MONTHLY": my_general.Timeframe.MONTHLY
        }

        start_moment = user_start_moment
        end_moment = user_end_moment
        time_frame = const_time_frame.get(user_time_frame)

        print("start_moment: ", start_moment)
        print("end_moment: ", end_moment)
        print("time_frame: ", time_frame)

        exporter = my_general.Exporter()

        if len(list_name_tickers) < 1:
            print("Error : len(list_name_stocks) < 1")
            return -1

        curr_path = root_path + '\\data\\'
        t_i = []
        i = 0
        for ticker in list_name_tickers:
            my_general.time.sleep(1)  # sec
            ticker_data = exporter.lookup(code=ticker, market=my_general.Market.SHARES,
                                          name_comparator=my_general.LookupComparator.EQUALS)
            data = exporter.download(id_=ticker_data.index[0], market=my_general.Market.SHARES, start_date=start_moment,
                                     timeframe=time_frame)
            data.to_csv(curr_path + 'target_ticker_' + ticker + '.csv')

            # print(data)
            file_name_tickers = 'print_graph_'

            date_value = data.get('<DATE>')
            time_value = data.get('<TIME>')
            open_value = data.get('<OPEN>')
            close_value = data.get('<CLOSE>')
            high_value = data.get('<HIGH>')
            low_value = data.get('<LOW>')
            volume_value = data.get('<VOL>')

            list_date_value = date_value.to_list()
            list_time_value = time_value.to_list()
            list_open_value = open_value.to_list()
            list_close_value = close_value.to_list()
            list_high_value = high_value.to_list()
            list_low_value = low_value.to_list()
            list_volume_value = volume_value.to_list()

            # Convert price to %
            max_val = max(list_close_value)

            j = 0
            t_i.append([])
            while j < len(list_close_value):
                list_close_value[j] = (list_close_value[j] * 100) / max_val
                # print("Before: ", list_date_value[j])
                buf_Y = str(list_date_value[j])
                buf_M = str(list_date_value[j])
                buf_D = str(list_date_value[j])
                buf_h = str(list_date_value[j])
                buf_m = str(list_date_value[j])
                list_date_value[j] = ""
                buf_Y = buf_Y[:4] + "-"
                buf_M = buf_M[4:6] + "-"
                buf_D = buf_D[-2:]
                list_date_value[j] = buf_Y + buf_M + buf_D
                # print("After: ", list_date_value[j])
                t_i[i].append(str(list_date_value[j]) + ' ' + str(list_time_value[j]))
                # print(t_i[i][j])

                j += 1

            list_tickers.append({"date_value": list_date_value,
                                 "time_value": list_time_value,
                                 "open_value": list_open_value,
                                 "close_value": list_close_value,
                                 "high_value": list_high_value,
                                 "low_value": list_low_value,
                                 "volume_value": list_volume_value})

            if len(list_open_value) < 1:
                print("It's time little boy!")
                return

            my_general.write_data_json(list_tickers,
                                       curr_path, file_name_tickers + str(list_name_tickers[i]))

            # _________________________________________________________________________________

            # Check on repeat
            hash_market = my_general.read_data_json(curr_path, 'hash_print_graph')

            file_name = 'hash_print_graph'
            new_hash = my_general.md5(curr_path + file_name + '.json')

            if new_hash == hash_market[0]["hash"]:
                print("___ No the new market values ___")
                return

            hash_market = [{"hash": new_hash}]
            file_name = 'hash_print_graph'
            my_general.write_data_json(hash_market, curr_path, file_name)

            i += 1

        # __________________________________ Load data _____________________________________

        curr_path = root_path + '\\'
        # Launch of script which get indicators
        my_general.exec_full(curr_path + "TA_stocks\\TA_stocks.py")

        # Load result_ta
        curr_path = root_path + '\\data\\'
        name_indicators = 'result_ta' + '_' + list_name_tickers[0]

        for indicator in list_name_indicators:
            name_indicators += '_' + indicator

        result_ta = my_general.read_data_json(curr_path, name_indicators)

        # Load tickers value
        curr_path = root_path + '\\data\\'

        i = 0
        for ticker in list_name_tickers:
            list_tickers.append({"close_value": my_general.read_data_json(curr_path,
                                                                          'print_graph_' + str(ticker))})
            i += 1

        # __________________________________ 2. Plot graph _____________________________________

        list_name_indicators.insert(0, list_name_tickers[0])

        my_general.gridsize = (len(list_name_indicators), 1)
        fig = my_general.plt.figure(figsize=(12, 8))

        i = 0
        axes = []
        while i < len(list_name_indicators):

            ax = my_general.plt.subplot2grid(my_general.gridsize, (i, 0))
            axes.append(ax)

            i += 1

        # style
        my_general.plt.style.use('seaborn-darkgrid')

        # Add labels to the plot
        style = dict(size=12, color='blue')

        # create a color palette
        palette = my_general.plt.get_cmap('Set1')

        font = {'family': 'serif',
                'color': 'darkred',
                'weight': 'normal',
                'size': 16,
                }

        axes[0].set_title("Analyze tickers", fontdict=font)

        axes[0].set_ylabel("Price, %", fontsize=9)
        axes[0].set_xlabel("time", fontsize=9)
        axes[0].grid(linestyle="--", color="gray", linewidth=0.5)

        # births['day'] = births['day'].astype(int)
        #
        # births.index = pd.to_datetime(10000 * births.year +
        #                               100 * births.month +
        #                               births.day, format='%Y%m%d')
        # births_by_date = births.pivot_table('births',
        #                                     [births.index.month, births.index.day])
        # births_by_date.index = [pd.datetime(2012, month, day)
        #                         for (month, day) in births_by_date.index]

        my_general.plt.gcf().autofmt_xdate()
        # left = 0.125  # the left side of the subplots of the figure
        # right = 0.9  # the right side of the subplots of the figure
        # bottom = 0.1  # the bottom of the subplots of the figure
        # top = 0.9  # the top of the subplots of the figure
        # wspace = 0.2  # the amount of width reserved for blank space between subplots
        # hspace = 0.2  # the amount of height reserved for white space between subplots
        my_general.plt.tight_layout() # subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
        m_time_format = my_general.mdates.date2num(t_i[0])

        axes[0].set_xticks(m_time_format[::100])  # для X оси берем в качестве тиков 1/10 часть дат из нашего фрейма

        #  делаем тики на оси X вертикальными
        xlabels = axes[0].xaxis.get_ticklabels()
        for label in xlabels:
            # цвет подписи делений оси OX
            label.set_color('blue')
            # поворот подписей делений оси OX
            label.set_rotation('vertical')
            # размер шрифта подписей делений оси OX
            label.set_fontsize(10)

        # форматирование дат для оси X  -
        # иначе вместо дат увидим просто чиселки (дни) григорианского календаря  с которыми matplotlib и работает внутри
        axes[0].xaxis.set_major_formatter(my_general.mdates.DateFormatter('%Y-%m-%d'))

        print("Time --> ", m_time_format)
        i = 0
        for it in list_name_tickers:
            # m_time_format
            axes[0].plot_date(m_time_format, #my_general.np.array(t_i[0]),
                         my_general.np.array(list_tickers[i]["close_value"]),
                         c=palette(i), linestyle='-',
                         label=it)

            i += 1

        axes[0].legend(loc='upper left', frameon=True)
        axes[0].text('2019-01-03 00:00:00', 60, "Bought", **style)
        axes[0].text('2020-09-02 00:00:00', 70, "Sold", ha='center', **style)

        # Get name indicators from array

        i = 0
        list_keys_indicators = []
        while i < len(result_ta):
            list_keys_indicators += result_ta[i].keys()
            i += 1

        list_name_indicators.pop(0)
        sublist_keys = []

        # print("----1> ", list_keys_indicators)
        # print("----2> ", list_name_indicators)

        i = 0
        vector_sizes = []
        while i < len(list_name_indicators):

            j = 0
            cnt = 0
            sublist_keys.append([])
            while j < len(list_keys_indicators):

                try:
                    index = list_keys_indicators[j].index('_')
                    buffer_key = list_keys_indicators[j][:index]
                except ValueError:
                    buffer_key = list_keys_indicators[j][:]

                # print("----1> ", list_keys_indicators[j])
                # print("----2> ", list_name_indicators[i].lower())
                if list_name_indicators[i].lower() == buffer_key:
                    sublist_keys[i].append(list_keys_indicators[j])
                    cnt += 1
                    # print("----3> ")

                j += 1

            vector_sizes.append(cnt)
            i += 1

        # print("----------> ", len(axes)) # 5
        # print("----------> ", list_name_indicators) # ['MACD', 'RSI', 'ATR', 'EMA']
        # print("----------> ", list_keys_indicators) # ['atr_i', 'ema_i', 'macd', 'macd_diff', 'macd_sig', 'rsi_i']
        # print("----------> ", sublist_keys) # [['macd', 'macd_diff', 'macd_sig'], ['rsi_i'], ['atr_i'], ['ema_i']]
        # print("----------> ", vector_sizes)
        i = 1
        while i <= len(list_name_indicators):

            axes[i].set_ylabel(list_name_indicators[i-1], fontsize=9)
            axes[i].grid(linestyle="--", color="gray", linewidth=0.5)

            j = 0
            while j < vector_sizes[i-1]:

                try:
                    # print("----------2> ", result_ta[i-1].keys())
                    # print("----------2> ", sublist_keys[i-1][j])
                    # print("----------2> ", j)

                    buffer_values = result_ta[i-1].get(sublist_keys[i-1][j])

                    axes[i].plot(my_general.np.asarray(buffer_values), c=palette(j),
                                 linestyle='solid', label=sublist_keys[i-1][j])

                except IndexError:
                    print("ValueError")
                    continue

                j += 1

            axes[i].legend(loc='upper left', frameon=True)

            i += 1

        my_general.plt.legend()
        my_general.plt.show()

    # def print_active_bids(self, depart_market): TODO (2)


def main():

    # Empty portfolio
    my_portfolio = Portfolio()

    print("____________________________________ PUT MONEY ____________________________________\n")

    # Download list of operations from backup file
    list_money_movement = my_general.read_data_json(root_path + '\\data\\', 'money_movement')

    # Update list of operations
    my_portfolio.copy_money_operations(Money(list_money_movement))

    my_portfolio.curr_money.deposit_funds(16000.0)  # set money to portfolio : TRUE
    my_portfolio.curr_money.withdraw_funds(16000.5)  # get money from portfolio : TRUE

    my_portfolio.curr_money.withdraw_funds(16000000)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(0)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(0.000001)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(0.1)  # CHECK : TRUE
    my_portfolio.curr_money.withdraw_funds(0.01)  # CHECK : TRUE
    my_portfolio.curr_money.withdraw_funds(0.9)  # CHECK : TRUE
    my_portfolio.curr_money.withdraw_funds(0.99)  # CHECK : TRUE
    my_portfolio.curr_money.withdraw_funds(0.991)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(-0.91)  # CHECK : FALSE
    my_portfolio.curr_money.withdraw_funds(-0.0001)  # CHECK : FALSE

    # my_portfolio.curr_money.withdraw_all_funds()  # CHECK : TRUE
    my_portfolio.curr_money.withdraw_funds(15998.0)  # CHECK : TRUE
    # my_portfolio.curr_money.withdraw_all_funds_plus_taxes(self):  # out all + taxes (13%) TODO (4)

    print("\n_______________________________________________________________________________________________________\n")

    my_portfolio.curr_money.deposit_funds(20000.0)  # CHECK : TRUE
    my_portfolio.curr_money.deposit_funds(0.0)  # CHECK : FALSE
    my_portfolio.curr_money.deposit_funds(0.000001)  # CHECK : FALSE
    my_portfolio.curr_money.deposit_funds(0.1)  # CHECK : TRUE)
    my_portfolio.curr_money.deposit_funds(0.01)  # CHECK : TRUE
    my_portfolio.curr_money.deposit_funds(0.9)  # CHECK : TRUE
    my_portfolio.curr_money.deposit_funds(0.99)  # CHECK : TRUE
    my_portfolio.curr_money.deposit_funds(0.991)  # CHECK : FALSE
    my_portfolio.curr_money.deposit_funds(-0.9)  # CHECK : FALSE

    print("\n____________________________________ BUY ____________________________________\n")

    name_ticker = ['MAIL']
    depart_market = 'STCK'
    my_general.name_tickers = name_ticker
    my_general.depart_market = depart_market

    # Launch of script which parse MOEX
    my_general.exec_full(path_name_parser_stocks)

    # Get info of ticker in the moment
    list_cur_val = my_general.read_data_json(root_path + '\\data\\', 'market')

    # Pseudo converting list to object
    info_ticker = {
        "ticker_value": list_cur_val[0][0]["ticker_value"],
        "date_value": list_cur_val[0][0]["date_value"],
        "time_value": list_cur_val[0][0]["time_value"],
        "last_value": list_cur_val[0][0]["last_value"]
    }

    print("Current bid : ", info_ticker)

    count_actives = 1

    bid = Bid('B', 'MAIL', info_ticker["last_value"], count_actives, 'STCK')
    my_portfolio.buy(bid)

    # print("Current cost assets --------> ", my_portfolio.current_profit_ticker(name_ticker, depart_market))
    # print("Current cost assets percent --------> ", my_portfolio.current_profit_ticker_percent(name_ticker, depart_market))
    # print("Current cost all assets --------> ", my_portfolio.cost_all_assets())
    # print("Share assets portfolio percent --------> ", my_portfolio.share_assets_portfolio_percent())
    # print("Current profit all --------> ", my_portfolio.current_profit_all())
    # print("Current profit all to percent --------> ", my_portfolio.current_profit_all_percent())
    # print("Print list current assets --------> ", my_portfolio.print_list_current_assets())
    # print("Print market --------> ", my_portfolio.print_market(depart_market))

    start_moment = my_general.datetime.date(2019,
                                            1,
                                            1)
    end_moment = my_general.datetime.date(my_general.datetime.datetime.now().year,
                                          my_general.datetime.datetime.now().month,
                                          my_general.datetime.datetime.now().day)

    print("Print graph --------> ", my_portfolio.print_graph(list_name_tickers=['TATN', 'NVTK'],
                                                             depart_market=depart_market,
                                                             list_name_indicators=['MACD', 'RSI', 'ATR', 'EMA'],
                                                             user_start_moment=start_moment,
                                                             user_end_moment=end_moment,
                                                             user_time_frame='DAILY'))

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
