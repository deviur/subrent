import logging

from typing import List, Dict

from subrent import db, Categories, exceptions


def import_json(data: List[Dict]) -> int:
    logging.debug(f'{len(data)=}')
    import_keys = "created date income outcome".split()

    categories = Categories()
    logging.debug(f"{len(categories)=}, {categories.get_category(0)=}")

    count = 0
    for dict_row in data:
        if dict_row['deleted']:
            continue
        transaction = {key: value for key, value in dict_row.items() if key in import_keys}
        try:
            category = categories.get_category_by_tags(dict_row['tag'])
            transaction['category_id'] = category.id
        except exceptions.UnknownTagId:
            continue

        db.insert('transactions', transaction)
        count += 1

    return count
