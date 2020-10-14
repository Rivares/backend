# coding: UTF-8

from finam.exception import * # noqa
from finam.const import * # noqa
from finam.export import * # noqa

import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from openpyxl import Workbook
from threading import Thread
from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np
import pymorphy2
import requests
import datetime
import logging
import hashlib
import random
import math
import time
import xlrd
import json
import csv
import sys
import os
import re
import ta


name_ticker = ''
depart_market = ''
root_path = ''


def exec_full(file_path, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": file_path,
        "__name__": "__main__",
    })
    with open(file_path, 'rb') as file:
        exec(compile(file.read(), file_path, 'exec'), globals, locals)


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def write_data_json(data, path, file_name):
    extension = '.json'

    with open(path + file_name + extension, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def read_data_json(path, file_name):
    extension = '.json'
    data = []
    # print(path + file_name + extension)
    with open(path + file_name + extension, encoding="utf-8") as json_file:
        data = json.load(json_file)

    return data


def convert_csv_to_xls(file_name):
    wb = Workbook()
    ws = wb.active
    with open(file_name + '.csv', 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save(file_name + '.xlsx')


def convert_json_to_xlsx(path_with_name):
    from_extension = '.json'
    to_extension = '.xlsx'

    pd.read_json(path_with_name + from_extension, encoding="utf-8").to_excel(path_with_name + to_extension, encoding="utf-8")


# ______________________________ NN ______________________________


def list_true_value(list_values_to_nn):
    list_diff_values = []
    prev_value = list_values_to_nn[0]
    for idx in range(1, len(list_values_to_nn)):
        if list_values_to_nn[idx] > prev_value: # prev_value + 3%
            list_diff_values.append(1)

        if list_values_to_nn[idx] < prev_value: # prev_value + 3%
            list_diff_values.append(-1)

        if list_values_to_nn[idx] == prev_value:
            list_diff_values.append(0)

        prev_value = list_values_to_nn[idx]

    return list_diff_values


