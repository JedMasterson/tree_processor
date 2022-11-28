class TreeProcessor:
    items = None

    def __init__(self, items_list: list):
        self.items = items_list

    def get_all(self):
        return self.items

    def get_item(self, item_id: int):
        item = list(filter(lambda x: x["id"] == item_id, self.items))
        try:
            item = item[0]
            return item
        except:
            return None

    def get_children(self, item_id: int):
        child_list = list(filter(lambda item: item["parent"] == item_id, self.items))
        return child_list

    def get_all_parents(self, item_id: int):
        parents_list = []
        current_parent = self.get_item(item_id)["parent"]
        while True:
            cur = self.get_item(current_parent)
            if cur:
                parents_list.append(cur)
                current_parent = cur["parent"]
            else:
                break

        return parents_list
