import pandas as pd


def find_magical_dates(start_date, end_date):
    magical_dates = []
    dates = pd.date_range(start_date, end_date, freq='D')
    magical_dates = dates[dates.map(
        lambda date: date.day * date.month == date.year % 100)]
    # for date in dates:
    #     if date.day * date.month == date.year % 100:
    #         magical_dates.append(date)
    return magical_dates


start_date = input('Введите дату начала (YYYY/MM/DD): ')  # 1901/01/01
end_date = input('Введите дату окончания (YYYY/MM/DD): ')  # 2000/12/31
print(
    f'Список магических дат:\n{pd.Series(find_magical_dates(start_date, end_date))}')
