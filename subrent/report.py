import os

from typing import List, Tuple
from string import Template
from subrent import transactions, date_helper as d

MONTHLY_PLAN = 148000 + 35250 + 1950 + 3000 + 8300


def make_report(date: str) -> str:
    daily_incomes = transactions.get_daily_incomes(date)
    daily_total_income = transactions.get_daily_total_income(date)
    monthly_plan_realization = transactions.get_monthly_total_income(date) - MONTHLY_PLAN
    daily_plan = -monthly_plan_realization/(d.get_month_end(date) - d.get_day(date))
    monthly_total_deposit = transactions.get_monthly_total_deposit(date)

    with open(os.path.join("db", "report_template.tpl"), 'r') as f:
        template = Template(f.read())
        keys = "date daily_incomes daily_total_income " \
               "monthly_plan_realization daily_plan monthly_total_deposit".split()
        values = [date,
                  make_string(daily_incomes),
                  f"{daily_total_income:+10.0f}",
                  f"{monthly_plan_realization:+10.0f}",
                  f"{daily_plan:+10.0f}",
                  f"{monthly_total_deposit:+10.0f}"
                  ]

    return template.safe_substitute(dict(zip(keys, values)))


def make_string(incomes: List[Tuple]) -> str:
    result = ''
    for income in incomes:
        result += f"{income[1]:+10.0f} ({income[2]})\n"
    return result[:-1]
