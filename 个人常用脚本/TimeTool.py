import datetime


def now(fmt='%Y%m%d%H%M%S'):
    string = datetime.datetime.now().strftime(fmt)
    return string


def string_to_date(string, fmt='%Y-%m-%d %H:%M:%S'):
    # 2021-01-28 10:51:26
    date = datetime.datetime.strptime(string, fmt)
    return date


def date_to_string(date, fmt='%Y-%m-%d %H:%M:%S'):
    # 2021-01-28 10:51:26
    string = date.strftime(fmt)
    return string
