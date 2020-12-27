# coding: UTF-8

import lib_general as my_general

root_path = my_general.root_path

curr_path = root_path + '\\data\\'

start = my_general.datetime.date(my_general.datetime.datetime.now().year - 1,
                                 my_general.datetime.datetime.now().month,
                                 my_general.datetime.datetime.now().day)

curr_moment = my_general.datetime.date(my_general.datetime.datetime.now().year,
                                       my_general.datetime.datetime.now().month,
                                       my_general.datetime.datetime.now().day)


def main():

    print("\n                TA __________________ --->\n")

    target_ticker = my_general.name_tickers[0]
    list_indicators_target_ticker = []

    # Load ticker of values
    df = my_general.pd.read_csv(curr_path + 'target_ticker_' + target_ticker + '.csv', sep=',')

    # Clean NaN values
    df = my_general.ta.utils.dropna(df)

    # Get indicators

    for it_indicator in my_general.indicators_market:

        if it_indicator == 'BB':

            # _____________________________________________________________________________________________________
            # _______________________________________ Volatility Inidicators ______________________________________
            # _____________________________________________________________________________________________________
            # __________________________________________ Bollinger Bands __________________________________________

            # Initialize Bollinger Bands Indicator
            indicator_bb = my_general.ta.volatility.BollingerBands(close=df["<CLOSE>"], window=20, ndev=2, fillna=True)

            # Add Bollinger Bands features
            df['bb_bbm'] = indicator_bb.bollinger_mavg()
            df['bb_bbh'] = indicator_bb.bollinger_hband()
            df['bb_bbl'] = indicator_bb.bollinger_lband()

            # Add Bollinger Band high indicator
            df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

            # Add Bollinger Band low indicator
            df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()

            # Add width size Bollinger Bands
            df['bb_bbw'] = indicator_bb.bollinger_wband()

            # print(df.columns)
            #
            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['bb_bbh'], label='High BB')
            # plt.plot(df['bb_bbl'], label='Low BB')
            # plt.plot(df['bb_bbm'], label='EMA BB')
            # plt.title('Bollinger Bands')
            # plt.legend()
            # plt.show()

            bb_bbh = df['bb_bbh'].to_list()
            bb_bbl = df['bb_bbl'].to_list()
            bb_bbm = df['bb_bbm'].to_list()

            list_indicators_target_ticker.append({
                "bb_bbh": bb_bbh,
                "bb_bbl": bb_bbl,
                "bb_bbm": bb_bbm
            })

        if it_indicator == 'KC':

            # __________________________________________ Keltner Channel __________________________________________

            # Initialize Keltner Channel Indicator
            indicator_kc = my_general.ta.volatility.KeltnerChannel(high=df["<HIGH>"],
                                                                   low=df["<LOW>"], close=df["<CLOSE>"], window=20, fillna=True)

            # Add Keltner Channel features
            df['kc_kcc'] = indicator_kc.keltner_channel_central()
            df['kc_kch'] = indicator_kc.keltner_channel_hband()
            df['kc_kcl'] = indicator_kc.keltner_channel_lband()

            # Add Keltner Channel high indicator
            df['kc_bbhi'] = indicator_kc.keltner_channel_hband_indicator()

            # Add Keltner Channel low indicator
            df['kc_bbli'] = indicator_kc.keltner_channel_lband_indicator()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['kc_kcc'], label='Central KC')
            # plt.plot(df['kc_kch'], label='High KC')
            # plt.plot(df['kc_kcl'], label='Low KC')
            # plt.title('Keltner Channel')
            # plt.legend()
            # plt.show()

            kc_kcc = df['kc_kcc'].to_list()
            kc_kch = df['kc_kch'].to_list()
            kc_kcl = df['kc_kcl'].to_list()

            list_indicators_target_ticker.append({
                "kc_kcc": kc_kcc,
                "kc_kch": kc_kch,
                "kc_kcl": kc_kcl
            })

        if it_indicator == 'ATR':

            # ______________________________________ Average true range (ATR) __________________________________________

            # Initialize Average true range Indicator
            indicator_atr = my_general.ta.volatility.AverageTrueRange(high=df["<HIGH>"],
                                                                      low=df["<LOW>"],
                                                                      close=df["<CLOSE>"], window=20, fillna=True)

            # Add ATR indicator
            df['atr_i'] = indicator_atr.average_true_range()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['atr_i'], label='ATR')
            # plt.title('Average true range (ATR)')
            # plt.legend()
            # plt.show()

            atr_i = df['atr_i'].to_list()

            list_indicators_target_ticker.append({
                "atr_i": atr_i
            })

        if it_indicator == 'DC':

            # __________________________________________ Donchian Channel __________________________________________

            # Initialize Donchian Channel Indicator
            indicator_dc = my_general.ta.volatility.DonchianChannel(close=df["<CLOSE>"], window=20, fillna=True)

            # Add Donchian Channel features
            df['dc_dch'] = indicator_dc.donchian_channel_hband()
            df['dc_dcl'] = indicator_dc.donchian_channel_lband()

            # Add Donchian Channel high indicator
            df['dc_dchi'] = indicator_dc.donchian_channel_hband_indicator()

            # Add Donchian Channel low indicator
            df['dc_dcli'] = indicator_dc.donchian_channel_lband_indicator()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['dc_dch'], label='High DC')
            # plt.plot(df['dc_dcl'], label='Low DC')
            # plt.title('Donchian Channel')
            # plt.legend()
            # plt.show()

            dc_dch = df['dc_dch'].to_list()
            dc_dcl = df['dc_dcl'].to_list()

            list_indicators_target_ticker.append({
                "dc_dch": dc_dch,
                "dc_dcl": dc_dcl
            })

        if it_indicator == 'ADX':

            # _____________________________________________________________________________________________________
            # __________________________________________ Trend Indicators _________________________________________
            # _____________________________________________________________________________________________________
            # _____________________________ Average Directional Movement Index (ADX) ________________________________

            # Initialize ADX Indicator
            indicator_adx = my_general.ta.trend.ADXIndicator(high=df["<HIGH>"],
                                                             low=df["<LOW>"],
                                                             close=df["<CLOSE>"], window=20, fillna=True)

            # Add ADX features
            df['adx_aver'] = indicator_adx.adx()
            df['adx_DI_pos'] = indicator_adx.adx_pos()
            df['adx_DI_neg'] = indicator_adx.adx_neg()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['adx_aver'], label='ADX')
            # plt.plot(df['adx_DI_pos'], label='+DI')
            # plt.plot(df['adx_DI_neg'], label='-DI')
            # plt.title('ADX')
            # plt.legend()
            # plt.show()

            adx_aver = df['adx_aver'].to_list()
            adx_DI_pos = df['adx_DI_pos'].to_list()
            adx_DI_neg = df['adx_DI_neg'].to_list()

            list_indicators_target_ticker.append({
                "adx_aver": adx_aver,
                "adx_DI_pos": adx_DI_pos,
                "adx_DI_neg": adx_DI_neg
            })

        if it_indicator == 'AI':

            # _____________________________ Aroon Indicator ________________________________

            # Initialize ADX Indicator
            indicator_ai = my_general.ta.trend.AroonIndicator(close=df["<CLOSE>"], window=20, fillna=True)

            # Add ADX features
            df['ai_i'] = indicator_ai.aroon_indicator()
            df['ai_up'] = indicator_ai.aroon_up()
            df['ai_down'] = indicator_ai.aroon_down()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['ai_i'], label='Aroon Indicator')
            # plt.plot(df['ai_up'], label='Aroon Up Channel')
            # plt.plot(df['ai_down'], label='Aroon Down Channel')
            # plt.title('Aroon Indicator')
            # plt.legend()
            # plt.show()

            ai_i = df['ai_i'].to_list()
            ai_up = df['ai_up'].to_list()
            ai_down = df['ai_down'].to_list()

            list_indicators_target_ticker.append({
                "ai_i": ai_i,
                "ai_up": ai_up,
                "ai_down": ai_down
            })

        if it_indicator == 'CCI':

            # _____________________________ Commodity Channel Index (CCI) ________________________________

            # Initialize ADX Indicator
            indicator_ccl = my_general.ta.trend.CCIIndicator(high=df["<HIGH>"],
                                                             low=df["<LOW>"],
                                                             close=df["<CLOSE>"], window=20, c=5, fillna=True)

            # Add ADX features
            df['ccl_i'] = indicator_ccl.cci()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['ccl_i'], label='CCI')
            # plt.title('Commodity Channel Index (CCI)')
            # plt.legend()
            # plt.show()

            ccl_i = df['ccl_i'].to_list()

            list_indicators_target_ticker.append({
                "ccl_i": ccl_i
            })

        if it_indicator == 'DPO':

            # _____________________________ Detrended Price Oscillator (DPO) ________________________________

            # Initialize DPO Indicator
            indicator_dpo = my_general.ta.trend.DPOIndicator(close=df["<CLOSE>"], window=20, fillna=True)

            # Add DPO features
            df['dpo_i'] = indicator_dpo.dpo()

            # plt.plot(df['dpo_i'], label='DPO')
            # plt.title('Detrended Price Oscillator (DPO)')
            # plt.legend()
            # plt.show()

            dpo_i = df['dpo_i'].to_list()

            list_indicators_target_ticker.append({
                "dpo_i": dpo_i
            })

        if it_indicator == 'EMA':

            # _____________________________ Exponential Moving Average (EMA) ________________________________

            # Initialize EMA Indicator
            indicator_ema = my_general.ta.trend.EMAIndicator(close=df["<CLOSE>"], window=20, fillna=True)

            # Add EMA features
            df['ema_i'] = indicator_ema.ema_indicator()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['ema_i'], label='EMA')
            # plt.title('Exponential Moving Average (EMA)')
            # plt.legend()
            # plt.show()

            ema_i = df['ema_i'].to_list()

            list_indicators_target_ticker.append({
                "ema_i": ema_i
            })

        if it_indicator == 'Ichimoku':

            # _____________________________ Ichimoku Kinkō Hyō (Ichimoku) ________________________________

            # Initialize Ichimoku Indicator
            indicator_ichimoku = my_general.ta.trend.IchimokuIndicator(high=df["<HIGH>"],
                                                                       low=df["<LOW>"], n1=10, n2=20, n3=30, visual=False, fillna=True)

            # Add Ichimoku features
            df['ichimoku_a'] = indicator_ichimoku.ichimoku_a()
            df['ichimoku_b'] = indicator_ichimoku.ichimoku_b()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['ichimoku_a'], label='Senkou Span A (Leading Span A)')
            # plt.plot(df['ichimoku_b'], label='Senkou Span B (Leading Span B)')
            # plt.title('Ichimoku Kinkō Hyō (Ichimoku)')
            # plt.legend()
            # plt.show()

            ichimoku_a = df['ichimoku_a'].to_list()
            ichimoku_b = df['ichimoku_b'].to_list()

            list_indicators_target_ticker.append({
                "ichimoku_a": ichimoku_a,
                "ichimoku_b": ichimoku_b
            })

        if 'KST' == it_indicator:

            # _____________________________ KST Oscillator (KST Signal) ________________________________

            # Initialize KST Indicator
            indicator_kst = my_general.ta.trend.KSTIndicator(close=df["<CLOSE>"], r1=10, r2=20, r3=30, r4=40,
                                                             n1=10, n2=10, n3=10, n4=15, nsig=9, fillna=True)
            # Add KST features
            df['kst'] = indicator_kst.kst()
            df['kst_diff'] = indicator_kst.kst_diff()
            df['kst_sig'] = indicator_kst.kst_sig()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['kst'], label='Know Sure Thing (KST)')
            # plt.plot(df['kst_diff'], label='Diff Know Sure Thing (KST)')
            # plt.plot(df['kst_sig'], label='Signal Line Know Sure Thing (KST)')
            # plt.title('KST Oscillator (KST Signal)')
            # plt.legend()
            # plt.show()

            kst = df['kst'].to_list()
            kst_diff = df['kst_diff'].to_list()
            kst_sig = df['kst_sig'].to_list()

            list_indicators_target_ticker.append({
                "kst": kst,
                "kst_diff": kst_diff,
                "kst_sig": kst_sig
            })

        if 'MACD' == it_indicator:

            # ____________________________ Moving Average Convergence Divergence (MACD) _______________________________

            # Initialize MACD Indicator
            indicator_macd = my_general.ta.trend.MACD(close=df["<CLOSE>"], window_fast=26, window_slow=12, window_sign=9, fillna=True)
            # Add MACD features
            df['macd'] = indicator_macd.macd()
            df['macd_diff'] = indicator_macd.macd_diff()
            df['macd_sig'] = indicator_macd.macd_signal()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['macd'], label='MACD Line')
            # plt.plot(df['macd_diff'], label='MACD Histogram')
            # plt.plot(df['macd_sig'], label='Signal Line')
            # plt.title('Moving Average Convergence Divergence (MACD)')
            # plt.legend()
            # plt.show()

            macd = df['macd'].to_list()
            macd_diff = df['macd_diff'].to_list()
            macd_sig = df['macd_sig'].to_list()

            i = 0
            while i < len(macd):
                macd[i] = macd[i] * (-1)
                macd_diff[i] = macd_diff[i] * (-1)
                macd_sig[i] = macd_sig[i] * (-1)

                i += 1

            list_indicators_target_ticker.append({
                "macd": macd,
                "macd_diff": macd_diff,
                "macd_sig": macd_sig
            })

        if 'MI' == it_indicator:

            # _____________________________ Mass Index (MI) ________________________________

            # Initialize MI Indicator
            indicator_mi = my_general.ta.trend.MassIndex(high=df["<HIGH>"], low=df["<LOW>"], window=10, n2=20, fillna=True)
            # Add MI features
            df['mi'] = indicator_mi.mass_index()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['mi'], label='Mass Index (MI)')
            # plt.title('Mass Index (MI)')
            # plt.legend()
            # plt.show()

            mi = df['mi'].to_list()

            list_indicators_target_ticker.append({
                "mi": mi
            })

        if 'P_SAR' == it_indicator:

            # _____________________________ Parabolic Stop and Reverse (Parabolic SAR) ________________________________

            # Initialize PSAR Indicator
            indicator_psar = my_general.ta.trend.PSARIndicator(high=df["<HIGH>"],
                                                               low=df["<LOW>"],
                                                               close=df["<CLOSE>"], step=0.02, max_step=0.2)

            # Add PSAR features
            df['psar_i'] = indicator_psar.psar()
            df['psar_up'] = indicator_psar.psar_up()
            df['psar_down'] = indicator_psar.psar_down()

            df['psar_up_i'] = indicator_psar.psar_up_indicator()
            df['psar_down_i'] = indicator_psar.psar_down_indicator()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['psar_i'], label='PSAR value')
            # plt.plot(df['psar_up'], label='PSAR up trend value')
            # plt.plot(df['psar_down'], label='PSAR down trend value')
            # plt.title('Parabolic Stop and Reverse (Parabolic SAR)')
            # plt.legend()
            # plt.show()

            psar_i = df['psar_i'].to_list()
            psar_up = df['psar_up'].to_list()
            psar_down = df['psar_down'].to_list()

            list_indicators_target_ticker.append({
                "psar_i": psar_i,
                "psar_up": psar_up,
                "psar_down": psar_down
            })

        if 'TRIX' == it_indicator:

            # _____________________________ Trix (TRIX) ________________________________

            # Initialize TRIX Indicator
            indicator_trix = my_general.ta.trend.TRIXIndicator(close=df["<CLOSE>"], window=15, fillna=True)

            # Add TRIX features
            df['trix_i'] = indicator_trix.trix()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['trix_i'], label='TRIX')
            # plt.title('Trix (TRIX)')
            # plt.legend()
            # plt.show()

            trix_i = df['trix_i'].to_list()

            list_indicators_target_ticker.append({
                "trix_i": trix_i
            })

        if 'VI' == it_indicator:

            # _____________________________ Vortex Indicator (VI) ________________________________

            # Initialize VI Indicator
            indicator_vi = my_general.ta.trend.VortexIndicator(high=df["<HIGH>"],
                                                               low=df["<LOW>"],
                                                               close=df["<CLOSE>"], window=15, fillna=True)

            # Add VI features
            df['vi_diff'] = indicator_vi.vortex_indicator_diff()
            df['vi_neg'] = indicator_vi.vortex_indicator_neg()
            df['vi_pos'] = indicator_vi.vortex_indicator_pos()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['vi_diff'], label='Diff VI')
            # plt.plot(df['vi_neg'], label='-VI')
            # plt.plot(df['vi_pos'], label='+VI')
            # plt.title('Vortex Indicator (VI)')
            # plt.legend()
            # plt.show()

            vi_diff = df['vi_diff'].to_list()
            vi_neg = df['vi_neg'].to_list()
            vi_pos = df['vi_pos'].to_list()

            list_indicators_target_ticker.append({
                "vi_diff": vi_diff,
                "vi_neg": vi_neg,
                "vi_pos": vi_pos
            })

        if 'CR' == it_indicator:

            # _____________________________________________________________________________________________________
            # _________________________________________ Others Indicators _________________________________________
            # _____________________________________________________________________________________________________
            # ______________________________________ Cumulative Return (CR) _______________________________________

            # Initialize CR Indicator
            indicator_cr = my_general.ta.others.CumulativeReturnIndicator(close=df["<CLOSE>"], fillna=True)

            # Add CR features
            df['cr_i'] = indicator_cr.cumulative_return()

            # plt.plot(df['cr_i'], label='Cumulative Return (CR)')
            # plt.title('Cumulative Return (CR)')
            # plt.legend()
            # plt.show()

            cr_i = df['cr_i'].to_list()

            list_indicators_target_ticker.append({
                "cr_i": cr_i
            })

        if 'DLR' == it_indicator:

            # ______________________________________ Daily Log Return (DLR) _______________________________________
            #
            # Initialize DLR Indicator
            indicator_dlr = my_general.ta.others.DailyLogReturnIndicator(close=df["<CLOSE>"], fillna=True)

            # Add DLR features
            df['dlr_i'] = indicator_dlr.daily_log_return()

            # plt.plot(df['dlr_i'], label='Daily Return (DR)')
            # plt.title('Daily Log Return (DLR)')
            # plt.legend()
            # plt.show()

            dlr_i = df['dlr_i'].to_list()

            list_indicators_target_ticker.append({
                "dlr_i": dlr_i
            })

        if 'ADI' == it_indicator:

            # _____________________________________________________________________________________________________
            # _________________________________________ Volume Indicators _________________________________________
            # _____________________________________________________________________________________________________
            # ______________________________ Accumulation/Distribution Index (ADI) ________________________________
            #
            # Initialize ADI Indicator
            indicator_adi = my_general.ta.volume.AccDistIndexIndicator(high=df["<HIGH>"],
                                                                       low=df["<LOW>"],
                                                                       close=df["<CLOSE>"], volume=df["<VOL>"], fillna=True)

            # Add ADI features
            df['adi_i'] = indicator_adi.acc_dist_index()

            # plt.plot(df['adi_i'], label='Accumulation/Distribution Index (ADI)')
            # plt.title('Accumulation/Distribution Index (ADI)')
            # plt.legend()
            # plt.show()

            adi_i = df['adi_i'].to_list()

            list_indicators_target_ticker.append({
                "adi_i": adi_i
            })

        if 'CMF' == it_indicator:

            # ______________________________ Chaikin Money Flow (CMF) ________________________________
            #
            # Initialize CMF Indicator
            indicator_cmf = my_general.ta.volume.ChaikinMoneyFlowIndicator(high=df["<HIGH>"],
                                                                           low=df["<LOW>"],
                                                                           close=df["<CLOSE>"],
                                                                           volume=df["<VOL>"], window=20, fillna=True)

            # Add CMF features
            df['cmf_i'] = indicator_cmf.chaikin_money_flow()

            # plt.plot(df['cmf_i'], label='CMF')
            # plt.title('Chaikin Money Flow (CMF)')
            # plt.legend()
            # plt.show()

            cmf_i = df['cmf_i'].to_list()

            list_indicators_target_ticker.append({
                "cmf_i": cmf_i
            })

        if 'EoM' == it_indicator:

            # ______________________________ Ease of movement (EoM, EMV) ________________________________

            # Initialize (EoM, EMV) Indicator
            indicator_eom = my_general.ta.volume.EaseOfMovementIndicator(high=df["<HIGH>"],
                                                                         low=df["<LOW>"],
                                                                         volume=df["<VOL>"], window=20, fillna=True)

            # Add (EoM, EMV) features
            df['eom_i'] = indicator_eom.ease_of_movement()
            df['eom_signal'] = indicator_eom.sma_ease_of_movement()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['cmf_i'], label='Ease of movement (EoM, EMV)')
            # plt.plot(df['cmf_signal'], label='Signal Ease of movement (EoM, EMV)')
            # plt.title('Ease of movement (EoM, EMV)')
            # plt.legend()
            # plt.show()

            eom_i = df['eom_i'].to_list()
            eom_signal = df['eom_signal'].to_list()

            list_indicators_target_ticker.append({
                "eom_i": eom_i,
                "eom_signal": eom_signal
            })

        if 'FI' == it_indicator:

            # ______________________________ Force Index (FI) ________________________________
            #
            # Initialize FI Indicator
            indicator_fi = my_general.ta.volume.ForceIndexIndicator(close=df["<CLOSE>"],
                                                                    volume=df["<VOL>"], window=20, fillna=True)

            # Add FI features
            df['fi_i'] = indicator_fi.force_index()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['fi_i'], label='FI')
            # plt.title('Force Index (FI)')
            # plt.legend()
            # plt.show()

            fi_i = df['fi_i'].to_list()

            list_indicators_target_ticker.append({
                "fi_i": fi_i
            })

        if 'NVI' == it_indicator:

            # ______________________________ Negative Volume Index (NVI) ________________________________
            #
            # Initialize NVI Indicator
            indicator_nvi = my_general.ta.volume.NegativeVolumeIndexIndicator(close=df["<CLOSE>"],
                                                                              volume=df["<VOL>"], fillna=True)

            # Add NVI features
            df['nvi_i'] = indicator_nvi.negative_volume_index()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['nvi_i'], label='NVI')
            # plt.title('Negative Volume Index (NVI)')
            # plt.legend()
            # plt.show()

            nvi_i = df['nvi_i'].to_list()

            list_indicators_target_ticker.append({
                "nvi_i": nvi_i
            })

        if 'OBV' == it_indicator:

            # ______________________________ On-balance volume (OBV) ________________________________
            #
            # Initialize OBV Indicator
            indicator_obv = my_general.ta.volume.OnBalanceVolumeIndicator(close=df["<CLOSE>"],
                                                                          volume=df["<VOL>"], fillna=True)

            # Add OBV features
            df['obv_i'] = indicator_obv.on_balance_volume()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['obv_i'], label='OBV')
            # plt.title('On-balance volume (OBV)')
            # plt.legend()
            # plt.show()

            obv_i = df['obv_i'].to_list()

            list_indicators_target_ticker.append({
                "obv_i": obv_i
            })

        if 'VPT' == it_indicator:

            # ______________________________ Volume-price trend (VPT) ________________________________
            #
            # Initialize VPT Indicator
            indicator_vpt = my_general.ta.volume.VolumePriceTrendIndicator(close=df["<CLOSE>"],
                                                                           volume=df["<VOL>"], fillna=True)

            # Add VPT features
            df['vpt_i'] = indicator_vpt.volume_price_trend()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['vpt_i'], label='VPT')
            # plt.title('Volume-price trend (VPT)')
            # plt.legend()
            # plt.show()

            vpt_i = df['vpt_i'].to_list()

            list_indicators_target_ticker.append({
                "vpt_i": vpt_i
            })

        if 'AO' == it_indicator:

            # _____________________________________________________________________________________________________
            # ________________________________________ Momentum Indicators ________________________________________
            # _____________________________________________________________________________________________________
            # _________________________________________ Awesome Oscillator ________________________________________
            #
            # Initialize Awesome Oscillator Indicator
            indicator_ao = my_general.ta.momentum.AwesomeOscillatorIndicator(high=df["<HIGH>"],
                                                                             low=df["<LOW>"],
                                                                             s=5, len=34, fillna=True)

            # Add Awesome Oscillator features
            df['ao_i'] = indicator_ao.ao()

            # plt.plot(df['ao_i'], label='AO')
            # plt.title('Awesome Oscillator')
            # plt.legend()
            # plt.show()

            ao_i = df['ao_i'].to_list()

            list_indicators_target_ticker.append({
                "ao_i": ao_i
            })

        if 'KAMA' == it_indicator:

            # ________________________________ Kaufman’s Adaptive Moving Average (KAMA) __________________________________
            #
            # Initialize KAMA Indicator
            indicator_kama = my_general.ta.momentum.KAMAIndicator(close=df["<CLOSE>"],
                                                                  window=10,
                                                                  pow1=2, pow2=30, fillna=True)

            # Add KAMA features
            df['kama_i'] = indicator_kama.kama()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['kama_i'], label='KAMA')
            # plt.title('Kaufman’s Adaptive Moving Average (KAMA)')
            # plt.legend()
            # plt.show()

            kama_i = df['kama_i'].to_list()

            list_indicators_target_ticker.append({
                "kama_i": kama_i
            })

        if 'MFI' == it_indicator:

            # ________________________________ Money Flow Index (MFI) __________________________________
            #
            # Initialize MFI Indicator
            indicator_mfi = my_general.ta.momentum.MFIIndicator(high=df["<HIGH>"],
                                                                low=df["<LOW>"],
                                                                close=df["<CLOSE>"],
                                                                volume=df["<VOL>"],
                                                                window=14, fillna=True)

            # Add MFI features
            df['mfi_i'] = indicator_mfi.money_flow_index()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['mfi_i'], label='MFI')
            # plt.title('Money Flow Index (MFI)')
            # plt.legend()
            # plt.show()

            mfi_i = df['mfi_i'].to_list()

            list_indicators_target_ticker.append({
                "mfi_i": mfi_i
            })

        if 'ROC' == it_indicator:

            # ________________________________ Rate of Change (ROC) __________________________________
            #
            # Initialize ROC Indicator
            indicator_roc = my_general.ta.momentum.ROCIndicator(close=df["<CLOSE>"],
                                                                window=12, fillna=True)

            # Add ROC features
            df['roc_i'] = indicator_roc.roc()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['roc_i'], label='ROC')
            # plt.title('Rate of Change (ROC)')
            # plt.legend()
            # plt.show()

            roc_i = df['roc_i'].to_list()

            list_indicators_target_ticker.append({
                "roc_i": roc_i
            })

        if 'RSI' == it_indicator:

            # ________________________________ Relative Strength Index (RSI) __________________________________
            #
            # Initialize RSI Indicator
            indicator_rsi = my_general.ta.momentum.RSIIndicator(close=df["<CLOSE>"],
                                                                window=12, fillna=True)

            # Add RSI features
            df['rsi_i'] = indicator_rsi.rsi()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['rsi_i'], label='RSI')
            # plt.title('Relative Strength Index (RSI)')
            # plt.legend()
            # plt.show()

            rsi_i = df['rsi_i'].to_list()
            rsi_upper_limit = [70] * len(rsi_i)
            rsi_down_limit = [30] * len(rsi_i)

            list_indicators_target_ticker.append({
                "rsi_i": rsi_i,
                "rsi_upper_limit": rsi_upper_limit,
                "rsi_down_limit": rsi_down_limit
            })

        if 'STOCH' == it_indicator:

            # ________________________________ Stochastic Oscillator __________________________________
            # Initialize RSI Indicator
            indicator_stoch = my_general.ta.momentum.StochasticOscillator(high=df["<HIGH>"],
                                                                          low=df["<LOW>"],
                                                                          close=df["<CLOSE>"],
                                                                          window=14, fillna=True)

            # Add RSI features
            df['stoch_i'] = indicator_stoch.stoch()
            df['stoch_signal'] = indicator_stoch.stoch_signal()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['stoch_i'], label='Stochastic Oscillator')
            # plt.plot(df['stoch_signal'], label='Signal Stochastic Oscillator')
            # plt.title('Stochastic Oscillator')
            # plt.legend()
            # plt.show()

            stoch_i = df['stoch_i'].to_list()
            stoch_signal = df['stoch_signal'].to_list()

            list_indicators_target_ticker.append({
                "stoch_i": stoch_i,
                "stoch_signal": stoch_signal
            })

        if 'TSI' == it_indicator:

            # ________________________________ True strength index (TSI) __________________________________
            #
            # Initialize TSI Indicator
            indicator_tsi = my_general.ta.momentum.TSIIndicator(close=df["<CLOSE>"],
                                                                r=25, s=13, fillna=True)

            # Add TSI features
            df['tsi_i'] = indicator_tsi.tsi()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['tsi_i'], label='TSI')
            # plt.title('True strength index (TSI)')
            # plt.legend()
            # plt.show()

            tsi_i = df['tsi_i'].to_list()

            list_indicators_target_ticker.append({
                "tsi_i": tsi_i,
                "tsi_i": tsi_i
            })

        if 'UO' == it_indicator:

            # ________________________________ Ultimate Oscillator __________________________________
            # Initialize Ultimate Oscillator Indicator
            indicator_uo = my_general.ta.momentum.UltimateOscillator(high=df["<HIGH>"],
                                                                     low=df["<LOW>"],
                                                                     close=df["<CLOSE>"],
                                                                     s=7,
                                                                     m=14, len=28, ws=4.0, wm=2.0, wl=1.0, fillna=True)

            # Add Ultimate Oscillator features
            df['uo_i'] = indicator_uo.uo()

            # # plt.plot(df["<CLOSE>"])
            # plt.plot(df['uo_i'], label='UO')
            # plt.title('Ultimate Oscillator')
            # plt.legend()
            # plt.show()

            uo_i = df['uo_i'].to_list()

            list_indicators_target_ticker.append({
                "uo_i": uo_i
            })

        if 'WR' == it_indicator:

            # ________________________________ Williams %R __________________________________
            # Initialize Williams Indicator
            indicator_wr = my_general.ta.momentum.WilliamsRIndicator(high=df["<HIGH>"],
                                                                     low=df["<LOW>"],
                                                                     close=df["<CLOSE>"],
                                                                     lbp=14, fillna=True)

            # Add Williams features
            df['wr_i'] = indicator_wr.wr()

            # plt.plot(df["<CLOSE>"])
            # plt.plot(df['wr_i'], label='Williams')
            # plt.title('Williams %R')
            # plt.legend()
            # plt.show()

            wr_i = df['wr_i'].to_list()

            list_indicators_target_ticker.append({
                "wr_i": wr_i
            })

    # Write to file

    file_name_ta = 'result_ta'
    name_ta = my_general.name_tickers[0]

    i = 0
    while i < len(my_general.indicators_market):
        name_ta += '_' + my_general.indicators_market[i]
        i += 1

    my_general.write_data_json(list_indicators_target_ticker, curr_path, file_name_ta + '_' + name_ta)

    print("\n__________________ TA __________________ <---\n")


if __name__ == '__main__':
    my_general.logging.basicConfig(level=my_general.logging.DEBUG)
    main()
