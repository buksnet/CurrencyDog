import cbrFetcher
from cbrFetcher import pd


def fetch_dollar():
    url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={cbrFetcher.then.strftime("%d/%m/%Y")}&date_req2={cbrFetcher.today.strftime("%d/%m/%Y")}&VAL_NM_RQ=R01235'
    dataset = pd.read_xml(url)
    dataset = dataset.drop(['Id', 'Nominal', 'VunitRate'], axis=1)
    dataset['Value'] = dataset['Value'].replace(',', '.', regex=True)
    return dataset


def fetch_euro():
    url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={cbrFetcher.then.strftime("%d/%m/%Y")}&date_req2={cbrFetcher.today.strftime("%d/%m/%Y")}&VAL_NM_RQ=R01239'
    dataset = pd.read_xml(url)
    dataset = dataset.drop(['Id', 'Nominal', 'VunitRate'], axis=1)
    dataset['Value'] = dataset['Value'].replace(',', '.', regex=True)
    return dataset


def fetch_yen():
    url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={cbrFetcher.then.strftime("%d/%m/%Y")}&date_req2={cbrFetcher.today.strftime("%d/%m/%Y")}&VAL_NM_RQ=R01820'
    dataset = pd.read_xml(url)
    dataset = dataset.drop(['Id', 'Nominal', 'VunitRate'], axis=1)
    dataset['Value'] = dataset['Value'].replace(',', '.', regex=True)
    return dataset


def fetch_currency_codes():
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={cbrFetcher.today.strftime("%d/%m/%Y")}'
    dataset = pd.read_xml(url, encoding='cp1251')
    dataset = dataset.drop(['NumCode', 'Nominal', 'VunitRate'], axis=1)
    return dataset

