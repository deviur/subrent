from typing import NamedTuple, List

from subrent import db, exceptions


class Category(NamedTuple):
    id: int
    name: str
    type: int
    tag_id: str


class Categories:
    def __init__(self):
        self._categories = _load_categories()

    def __len__(self):
        return len(self._categories)

    def get_category(self, category_id: int) -> Category:
        return [category for category in self._categories if category.id == category_id][-1]

    def get_category_by_tags(self, tags: List[str]):
        if not tags:
            return self.get_category(0)

        for c in self._categories:
            if c.tag_id in tags:
                return self.get_category(c.id)

        raise exceptions.UnknownTagId


def _load_categories() -> List[Category]:
    categories = db.fetchall(
        "category", "id name type tag_id".split()
    )
    category_result = []
    for category in categories:
        category_result.append(Category(**category))

    return category_result
