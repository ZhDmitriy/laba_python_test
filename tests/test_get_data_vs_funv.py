import doctest
import pandas as pd
import os


def get_data_vs() -> None:
    """ Функция скачивает данные с ценами канала ВсеИнструменты

    >>> get_data_vs()
    success
    <class 'pandas.core.frame.DataFrame'>

    """
    data_vi = pd.read_excel(r"D:\prod_project\tests\vse_instruments.xlsx")

    path = r'C:/Users/janev/OneDrive/Desktop/tableau_vi/main/report_vse_instrument.xlsx' # путь сохранения файла
    data_vi.to_excel(path, index=False)

    if os.path.isfile(path):
        os.remove(path)
        print('success')
    else:
        print("Error! File doesn't exists!")

    return type(data_vi)


doctest.testmod()