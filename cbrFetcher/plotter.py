import datetime
import matplotlib.pyplot as plt

from datetime import datetime
from cbrFetcher.fetcher import fetch_dollar, fetch_euro, fetch_yen


def plot_dollar_only():
    plt.figure(figsize=(14, 8))

    dataframe = fetch_dollar()
    x = dataframe['Date']
    y = dataframe['Value'].astype(float)
    dates = [datetime.strptime(i, '%d.%m.%Y') for i in x]

    plt.plot_date(dates, y, linestyle='solid')
    plt.title('Курс Доллара за последние 30 дней')

    plt.legend(['Доллар'])
    plt.show()


def plot_many():
    plt.figure(figsize=(14, 8))
    plt.yticks(())

    dollar = fetch_dollar()
    euro = fetch_euro()
    yen = fetch_yen()

    for currency in [dollar, euro, yen]:
        x = currency['Date']
        y = currency['Value'].astype(float)
        dates = [datetime.strptime(i, '%d.%m.%Y') for i in x]
        plt.plot_date(dates, y, linestyle='solid')
    plt.title('Курс валют за последние 30 дней')

    plt.yticks([i for i in range(1, 131, 10)])

    plt.legend(['Доллар', 'Евро', 'Японская Йена'])
    plt.show()
