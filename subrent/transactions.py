from typing import Tuple, List

from subrent import db


def get_daily_incomes(day: str) -> List[Tuple]:
    cursor = db.get_cursor()
    cursor.execute(
        f"SELECT t.date, t.income - t.outcome, c.name "
        f"FROM transactions t LEFT JOIN category c "
        f"ON t.category_id = c.id "
        f"WHERE t.date = '{day}' AND c.type IN (0, 1)"
        f"ORDER BY t.created ASC"
    )
    return cursor.fetchall()


def get_daily_total_income(day: str) -> float:
    cursor = db.get_cursor()
    cursor.execute(
        f"SELECT sum(t.income) - sum(t.outcome) "
        f"FROM transactions t LEFT JOIN category c "
        f"ON t.category_id = c.id "
        f"WHERE date = '{day}' and c.type = 1"
    )
    result = cursor.fetchone()
    return result[0] if result[0] else 0.
