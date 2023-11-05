import doctest

LOGIN = 'd.zhdanov@tradebt.su'
PASSWORD_yandex = 'l7TrWrWc'

from email.header import decode_header
import imaplib
import email


# Часть модуля для дипломного проекта. Что-то осмысленное кроме валидации данных
# придумать сложно, так как логики здесь нет
def extract_data_one_c():
    """ Получаем данные о заказах и продажах из рассылки.

    >>> extract_data_one_c()
    [<class 'str'>, <class 'str'>, <class 'str'>]

    """
    mail_pass = 'qtrkdmionnpmrxuw'
    username = LOGIN
    imap_server = "imap.yandex.ru"

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select("ONE_C")  # имя папки

    list_letter = imap.search(None, 'ALL')
    list_let_res = list_letter[1][0].decode('utf-8').split(" ")
    letter_last = []

    for item in list_let_res:
        letter_last.append(int(item))

    res_last_letter = str(max(letter_last)).encode(encoding='utf-8')

    res, msg = imap.fetch(res_last_letter, '(RFC822)')
    msg = email.message_from_bytes(msg[0][1])

    letter_id = msg["Message-ID"]  # айди письма
    letter_from = msg["Return-path"]  # e-mail отправителя
    title_email = decode_header(msg["Subject"])[0][0].decode()  # заголовок письма

    return [type(letter_id), type(letter_from), type(title_email)]

doctest.testmod()
