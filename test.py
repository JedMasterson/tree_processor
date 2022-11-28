import pytest
from tree_processor import TreeProcessor


class TestClass:
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    processor = TreeProcessor(items)

    def test_create(self):
        tested_items = self.processor.get_all()
        assert tested_items == self.items

    def test_item(self):
        items_test = []
        for item in self.items:
            tested_item = self.processor.get_item(item["id"])
            example_item = item
            items_test.append(tested_item == example_item)
        test = all(flag == 1 for (flag) in items_test)
        assert test

    def test_children(self):
        example_item = self.items[1]
        expected_items = [self.items[3], self.items[4], self.items[5]]
        tested_children = self.processor.get_children(example_item['id'])
        assert tested_children == expected_items

    def test_parent(self):
        example_item = self.items[-1]
        expected_item = [self.items[3], self.items[1], self.items[0]]
        example_id = example_item["id"]
        tested_parent = self.processor.get_all_parents(example_item["id"])
        assert tested_parent == expected_item

