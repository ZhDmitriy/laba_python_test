import pandas as pd
import requests
import wget
import os
import json
from config import LOGIN, PASSWORD_yandex
import base64
from email.header import decode_header
import imaplib
import email


# Задание один
def example_one(x: bool, y: bool) -> bool:
    """
        Функция находит XOR между двумя переменными x и y
    """
    if x == True and y == True:
        return False
    elif (x == True and y == False) or (x == False and y == True):
        return True
    elif (x == False and y == False):
        return False


# Задание два
def example_two(num1: int, num2: int, num3: int, num4: int) -> int:
    """
        Функция находит минимальное число из четырех переданных
    """
    return min(min(num1, num2), min(num3, num4))


# Задание три
def example_three(num1: int, num2: int) -> int:
    """
        Функция находит максимум из двух чисел
    """
    return max(num1, num2)


# Модуль для дипломного проекта
def extract_data_price() -> pd.DataFrame:
    """
        Функция получает цены из личного кабинта пользователя Яндекс.Маркет
        Extract из ETL, функция из дата пайплана по обработке актуальных цен
        пользователя
    """
    sku_list = []
    price_list = []
    date_list = []

    headers = {
        'Authorization': 'Bearer y0_AgAAAAAwy8GyAAqafQAAAADuVES0dzOy_1rARlGU3LSBRVT0QoDJ9FA'
    }

    body_result = {"offerIds": ["121787"]}

    result = requests.get('https://api.partner.market.yandex.ru/campaigns/23415831/offer-prices?page_token=&limit=940',
                          headers=headers, data=body_result)

    for item in result.json()['result']['offers']:
        sku_list.append(item['id'])  # sku товара
        price_list.append(item['price']['value'])  # цена товара
        date_list.append(item['updatedAt'])  # цена на дату

    data_result = {'sku': sku_list, 'price': price_list, 'date': date_list}
    data_result = pd.DataFrame(data_result)

    # здесь для проверки чаще используются не как таковые результаты логики, а проверка данных: вместо
    # тестов используется валидация данных, полученных по json, если данные корректные, то значит тест пройден
    # для pytest можно проверить какой тип объекта вернулся

    return type(data_result)


def example_five(words_list_input: list) -> list:
    """
        Функция возвращает список из слов, которые встречались
        в тексте по ходу его чтения слева
    """

    dict_word = {}

    words_list = words_list_input.split(" ")
    count_word_in_words_list = []

    for item_word in words_list:
        dict_word[item_word] = 0

    for i_high, item_word in enumerate(words_list):
        if item_word in words_list[:i_high]:  # хранится история перебора слов
            dict_word[item_word] += 1
        count_word_in_words_list.append(dict_word[item_word])

    return count_word_in_words_list

result_words =  """She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."""


# Часть модуля для дипломного проекта
def extract_data_one_c():
    """ Получаем данные о заказах и продажах из рассылки  """
    mail_pass = 'qtrkdmionnpmrxuw'
    username = LOGIN
    imap_server = "imap.yandex.ru"

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select("ONE_C") # имя папки

    list_letter = imap.search(None, 'ALL')
    list_let_res = list_letter[1][0].decode('utf-8').split(" ")
    letter_last = []

    for item in list_let_res:
        letter_last.append(int(item))

    res_last_letter = str(max(letter_last)).encode(encoding='utf-8')

    res, msg = imap.fetch(res_last_letter, '(RFC822)')
    msg = email.message_from_bytes(msg[0][1])

    letter_id = msg["Message-ID"] #айди письма
    letter_from = msg["Return-path"] # e-mail отправителя
    title_email = decode_header(msg["Subject"])[0][0].decode() # заголовок письма

    return [letter_id, letter_from, title_email]


def get_data_vs() -> None:
    """ Функция скачивает данные с ценами канала ВсеИнструменты """
    data_vi = pd.read_excel(r"D:\prod_project\tests\vse_instruments.xlsx")

    path = r'C:/Users/janev/OneDrive/Desktop/tableau_vi/main/report_vse_instrument.xlsx' # путь сохранения файла

    if os.path.isfile(path):
        os.remove(path)
        print('success')
    else:
        print("Error! File doesn't exists!")

    return type(data_vi)