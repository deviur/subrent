import logging

from typing import List, Dict

from subrent import db


def import_json(data: List[Dict]) -> int:
    logging.debug(f'{len(data)=}')

    cursor = db.get_cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()

    logging.debug(f"{len(transactions)=}")
    return len(transactions)
