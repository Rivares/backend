# coding: UTF-8

import lib_general as my_general

root_path = my_general.root_path

curr_path = root_path + '\\data\\'

curr_moment = my_general.datetime.date(my_general.datetime.datetime.now().year,
                                       my_general.datetime.datetime.now().month,
                                       my_general.datetime.datetime.now().day)


def main():
    print("\n__________________ Parsing markets __________________\n")

    exporter = my_general.Exporter()

    market = []
    list_goods = []
    list_currency = []
    list_indexes = []
    list_etf = []
    list_stocks = []

    # print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~ Goods ~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    # GDS: Goods; CRNCY: Currency; INDXS_WR: Indexes(W+R); INDXS_WU: Indexes(W+U); STCK: Stock

    if my_general.depart_market == "GDS":
        list_name_goods = [
            'Brent',
            'Natural Gas',
            'Алюминий',
            'Бензин',
            'Золото',
            'Мазут',
            'Медь',
            'Никель',
            'Палладий',
            'Платина',
            'Пшеница',
            'Серебро'
        ]

        for goods in list_name_goods:
            my_general.time.sleep(1)  # sec
            # print('\n__________________ ' + goods + ' __________________\n')
            ticker = exporter.lookup(name=goods, market=my_general.Market.COMMODITIES,
                                     name_comparator=my_general.LookupComparator.EQUALS)
            data = exporter.download(ticker.index[0], market=my_general.Market.COMMODITIES, start_date=curr_moment)

            open_value = data.get('<OPEN>')
            close_value = data.get('<CLOSE>')
            high_value = data.get('<HIGH>')
            low_value = data.get('<LOW>')
            volume_value = data.get('<VOL>')

            list_open_value = open_value.to_list()
            list_close_value = close_value.to_list()
            list_high_value = high_value.to_list()
            list_low_value = low_value.to_list()
            list_volume_value = volume_value.to_list()

            list_goods.append({"open_value": list_open_value[-1],
                               "close_value": list_close_value[-1],
                               "high_value": list_high_value[-1],
                               "low_value": list_low_value[-1],
                               "volume_value": list_volume_value[-1]})

            # print(data.tail(1))

        # print(list_goods)
    elif my_general.depart_market == "CRNCY":
        # print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~ Currency ~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        list_name_currency = [
            'USDRUB_TOD',
            'EURRUB_TOD',
            'EURUSD_TOD',
            'CNYRUB_TOD'
        ]

        for currency in list_name_currency:
            my_general.time.sleep(1)  # sec
            # print('\n__________________ ' + currency + ' __________________\n')
            ticker = exporter.lookup(name=currency, market=my_general.Market.CURRENCIES,
                                     name_comparator=my_general.LookupComparator.EQUALS)
            data = exporter.download(ticker.index[0], market=my_general.Market.CURRENCIES, start_date=curr_moment)

            open_value = data.get('<OPEN>')
            close_value = data.get('<CLOSE>')
            high_value = data.get('<HIGH>')
            low_value = data.get('<LOW>')
            volume_value = data.get('<VOL>')

            list_open_value = open_value.to_list()
            list_close_value = close_value.to_list()
            list_high_value = high_value.to_list()
            list_low_value = low_value.to_list()
            list_volume_value = volume_value.to_list()

            list_currency.append({"open_value": list_open_value[-1],
                                  "close_value": list_close_value[-1],
                                  "high_value": list_high_value[-1],
                                  "low_value": list_low_value[-1],
                                  "volume_value": list_volume_value[-1]})
            # print(data.tail(1))


    elif my_general.depart_market == "INDXS_WR":
        # print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~ Indexes (World + Russia)~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        list_name_indexes_WR = [
            'CSI200 (Китай)',
            'CSI300 (Китай)',
            'Hang Seng (Гонконг)',
            'KOSPI (Корея)',
            'N225Jap*',
            'Shanghai Composite(Китай)',
            'Индекс МосБиржи',
            'Индекс МосБиржи 10',
            'Индекс МосБиржи голубых фишек',
            'Индекс МосБиржи инноваций',
            'Индекс МосБиржи широкого рынка',
            'Индекс РТС',
            'Индекс РТС металлов и добычи',
            'Индекс РТС нефти и газа',
            'Индекс РТС потреб. сектора',
            'Индекс РТС телекоммуникаций',
            'Индекс РТС транспорта',
            'Индекс РТС финансов',
            'Индекс РТС химии и нефтехимии',
            'Индекс РТС широкого рынка',
            'Индекс РТС электроэнергетики',
            'Индекс гос обл RGBI',
            'Индекс гос обл RGBI TR',
            'Индекс корп обл MOEX CBICP',
            'Индекс корп обл MOEX CBITR',
            'Индекс корп обл MOEX CP 3',
            'Индекс корп обл MOEX CP 5',
            'Индекс корп обл MOEX TR 3',
            'Индекс корп обл MOEX TR 5',
            'Индекс металлов и добычи',
            'Индекс мун обл MOEX MBICP',
            'Индекс мун обл MOEX MBITR',
            'Индекс нефти и газа',
            'Индекс потребит сектора',
            'Индекс телекоммуникаций',
            'Индекс транспорта',
            'Индекс финансов',
            'Индекс химии и нефтехимии',
            'Индекс электроэнергетики'
        ]

        for index in list_name_indexes_WR:
            my_general.time.sleep(1)  # sec
            try:
                # print('\n__________________ ' + index + ' __________________\n')
                ticker = exporter.lookup(name=index, market=my_general.Market.INDEXES,
                                         name_comparator=my_general.LookupComparator.EQUALS)

                data = exporter.download(ticker.index[0], market=my_general.Market.INDEXES, start_date=curr_moment)

                open_value = data.get('<OPEN>')
                close_value = data.get('<CLOSE>')
                high_value = data.get('<HIGH>')
                low_value = data.get('<LOW>')
                volume_value = data.get('<VOL>')

                list_open_value = open_value.to_list()
                list_close_value = close_value.to_list()
                list_high_value = high_value.to_list()
                list_low_value = low_value.to_list()
                list_volume_value = volume_value.to_list()

                list_indexes.append({"open_value": list_open_value[-1],
                                     "close_value": list_close_value[-1],
                                     "high_value": list_high_value[-1],
                                     "low_value": list_low_value[-1],
                                     "volume_value": list_volume_value[-1]})
            except:
                list_indexes.append({"open_value": 0.0,
                                     "close_value": 0.0,
                                     "high_value": 0.0,
                                     "low_value": 0.0,
                                     "volume_value": 0.0})
                print("Problem with – tickers(index) - " + index)

    elif my_general.depart_market == "INDXS_WU":
        # print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~ Indexes (World + USA)~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        list_name_indexes_W_U = [
            'D&J-Ind*',
            'NASDAQ 100**',
            'NASDAQ**',
            'SandP-500*'
        ]

        for index in list_name_indexes_W_U:

            # if (my_general.datetime.datetime.now().hour > 15) and (my_general.datetime.datetime.now().minute > 40):

            try:
                my_general.time.sleep(1)  # sec
                # print('\n__________________ ' + index + ' __________________\n')
                ticker = exporter.lookup(name=index, market=my_general.Market.INDEXES,
                                         name_comparator=my_general.LookupComparator.EQUALS)

                data = exporter.download(ticker.index[0], market=my_general.Market.INDEXES, start_date=curr_moment)

                open_value = data.get('<OPEN>')
                close_value = data.get('<CLOSE>')
                high_value = data.get('<HIGH>')
                low_value = data.get('<LOW>')
                volume_value = data.get('<VOL>')

                list_open_value = open_value.to_list()
                list_close_value = close_value.to_list()
                list_high_value = high_value.to_list()
                list_low_value = low_value.to_list()
                list_volume_value = volume_value.to_list()

                list_indexes.append({"open_value": list_open_value[-1],
                                     "close_value": list_close_value[-1],
                                     "high_value": list_high_value[-1],
                                     "low_value": list_low_value[-1],
                                     "volume_value": list_volume_value[-1]})
            # else:
            except:
                list_indexes.append({"open_value": 0.0,
                                     "close_value": 0.0,
                                     "high_value": 0.0,
                                     "low_value": 0.0,
                                     "volume_value": 0.0})

    elif my_general.depart_market == "ETF":  # Implementation -> my_general.name_ticker == '' TODO (3)
        # print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~ ETF ~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        list_name_etf = [
            'FXCN ETF',
            'FXDE ETF',
            'FXGD ETF',
            'FXKZ ETF',
            'FXMM ETF',
            'FXRB ETF',
            'FXRL ETF',
            'FXRU ETF',
            'FXRW ETF',
            'FXTB ETF',
            'FXUS ETF',
            'FXWO ETF',
            'RUSB ETF',
            'RUSE ETF',
            'SBCB ETF',
            'SBGB ETF',
            'SBMX ETF',
            'SBRB ETF',
            'SBSP ETF',
            'TRUR ETF',
            'VTBA ETF',
            'VTBB ETF',
            'VTBE ETF',
            'VTBH ETF',
            'VTBM ETF',
        ]

        for stock in list_name_etf:
            my_general.time.sleep(1)  # sec
            # print('\n__________________ ' + stock + ' __________________\n')
            ticker = exporter.lookup(name=stock, market=my_general.Market.ETF_MOEX,
                                     name_comparator=my_general.LookupComparator.EQUALS)
            data = exporter.download(ticker.index[0], market=my_general.Market.ETF_MOEX, start_date=curr_moment)

            open_value = data.get('<OPEN>')
            close_value = data.get('<CLOSE>')
            high_value = data.get('<HIGH>')
            low_value = data.get('<LOW>')
            volume_value = data.get('<VOL>')

            list_open_value = open_value.to_list()
            list_close_value = close_value.to_list()
            list_high_value = high_value.to_list()
            list_low_value = low_value.to_list()
            list_volume_value = volume_value.to_list()

            list_etf.append({"open_value": list_open_value[-1],
                             "close_value": list_close_value[-1],
                             "high_value": list_high_value[-1],
                             "low_value": list_low_value[-1],
                             "volume_value": list_volume_value[-1]})

    elif my_general.depart_market == "STCK":
        # print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~ Stock ~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        if len(my_general.name_tickers) < 1:
            list_name_stocks = [
                'ETLN',
                'QIWI',
                'TCSG',
                'FIVE',
                'AKRN',
                'ALRS',
                'AFLT',
                'BANE',
                'BSPB',
                'VSMO',
                'VTBR',
                'GAZP',
                'SIBN',
                'PIKK',
                'DSKY',
                'IRAO',
                'KBTK',
                'LNTA',
                'LSNG', 'LSNGР',
                'LSRG',
                'LKOH',
                'MVID',
                'MGNT',
                'MGTS', 'MGTSР',
                'MTLR', 'MTLRР',
                'CBOM',
                'MAGN',
                'MOEX',
                'MSTT',
                'MSNG',
                'MSRS',
                'MRKV',
                'MRKU',
                'MRKC',
                'MRKP',
                'MTSS',
                'NKNC', 'NKNCР',
                'NLMK',
                'NMTP',
                'NVTK',
                'GMKN',
                'OGKB',
                'POLY',
                'PLZL',
                'PRTK',
                'RASP',
                'ROSN',
                'RSTI', 'RSTIР',
                'RTKM', 'RTKMР',
                'AGRO',
                'RUAL',
                'HYDR',
                'RNFT',
                'SFIN',
                'SBER', 'SBERP',
                'CHMF',
                'AFKS',
                'SNGS', 'SNGSР',
                'TATN', 'TATNР',
                'TGKA',
                'TRMK',
                'TRNFP',
                'PHOR',
                'FEES',
                'GCHE',
                'ENRU',
                'UPRO',
                'MAIL',
                'YNDX',
                'INTC',
                'CSCO',
                'HPQ',
                'HPE',
                'T'
            ]
        else:
            list_name_stocks = my_general.name_tickers

        for stock in list_name_stocks:
            my_general.time.sleep(1)  # sec
            # print('\n__________________ ' + stock + ' __________________\n')
            ticker = exporter.lookup(code=stock, market=my_general.Market.SHARES,
                                     name_comparator=my_general.LookupComparator.EQUALS)
            data = exporter.download(id_=ticker.index[0], market=my_general.Market.SHARES, start_date=curr_moment,
                                     timeframe=my_general.Timeframe.TICKS)

            # print(data)
            ticker_value = data.get('<TICKER>')
            per_value = data.get('<PER>')
            date_value = data.get('<DATE>')
            time_value = data.get('<TIME>')
            last_value = data.get('<LAST>')
            volume_value = data.get('<VOL>')

            # open_value = data.get('<OPEN>')
            # close_value = data.get('<CLOSE>')
            # high_value = data.get('<HIGH>')
            # low_value = data.get('<LOW>')
            # volume_value = data.get('<VOL>')
            # print(ticker_value)
            # list_open_value = open_value.to_list()
            # list_close_value = close_value.to_list()
            # list_high_value = high_value.to_list()
            # list_low_value = low_value.to_list()
            # list_volume_value = volume_value.to_list()

            list_ticker_value = ticker_value.to_list()
            list_per_value = per_value.to_list()
            list_date_value = date_value.to_list()
            list_time_value = time_value.to_list()
            list_last_value = last_value.to_list()
            list_volume_value = volume_value.to_list()

            # list_stocks.append({"open_value": list_open_value[-1],
            #                     "close_value": list_close_value[-1],
            #                     "high_value": list_high_value[-1],
            #                     "low_value": list_low_value[-1],
            #                     "volume_value": list_volume_value[-1]})

            if len(list_ticker_value) > 0:
                list_stocks.append({"ticker_value": list_ticker_value[-1],
                                    "per_value": list_per_value[-1],
                                    "date_value": list_date_value[-1],
                                    "time_value": list_time_value[-1],
                                    "last_value": list_last_value[-1],
                                    "volume_value": list_volume_value[-1]})
            else:
                print("It's time little boy!")
                return

    # _________________________________________________________________________________

    if len(list_goods) > 0:
        market.append(list_goods);

    if len(list_currency) > 0:
        market.append(list_currency);

    if len(list_indexes) > 0:
        market.append(list_indexes)

    if len(list_etf) > 0:
        market.append(list_etf)

    if len(list_stocks) > 0:
        market.append(list_stocks)

    # print(market)
    file_name_market = 'market'

    my_general.write_data_json(market, curr_path, file_name_market)
    # _________________________________________________________________________________

    # Check on repeat
    hash_market = my_general.read_data_json(curr_path, 'hash_market')

    file_name = 'market'
    new_hash = my_general.md5(curr_path + 'market' + '.json')

    if new_hash == hash_market[0]["hash"]:
        print("___ No the new market values ___")
        return

    hash_market = [{"hash": new_hash}]
    file_name = 'hash_market'
    my_general.write_data_json(hash_market, curr_path, file_name)

    # _________________________________________________________________________________


if __name__ == '__main__':
    main()
