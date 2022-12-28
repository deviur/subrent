import os

from string import Template
from subrent import transactions


def make_report(date: str) -> str:
    with open(os.path.join("db", "report_template.tpl"), 'r') as f:
        template = Template(f.read())
        keys = "date daily_incomes daily_total_income".split()
        values = [date,
                  get_daily_incomes(date),
                  get_daily_total_income(date)
                  ]

    return template.safe_substitute(dict(zip(keys, values)))


def get_daily_incomes(date: str) -> str:
    result = ''
    for transaction in transactions.get_daily_incomes(date):
        result += f"{transaction[1]:+10.0f} ({transaction[2]})\n"
    return result.strip()


def get_daily_total_income(date: str) -> str:
    return f"{transactions.get_daily_total_income(date):+10.0f} (Субаренда)"
