import calendar


def get_day(date: str) -> int:
    return int(date[-2:])


def get_month(date: str) -> int:
    return int(date[5:7])


def get_year(date: str) -> int:
    return int(date[:4])


def get_month_end(date: str) -> int:
    return calendar.monthrange(get_year(date), get_month(date))[-1]
