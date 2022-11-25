class TreeStore:
    def __init__(self, items):
        self.items = items

    def get_all(self):
        return self.items

    def get_item(self, id):
        for item in self.items:
            if item['id'] == id:
                return item

    def get_children(self, id):
        lists = []
        for item in self.items:
            if item['parent'] == id:
                lists.append(item)
        return lists

    def get_all_parents(self, id):
        item = self.get_item(id)
        parent = self.get_item(item['parent'])
        lists = []
        while parent:
            lists.append(parent)
            parent = self.get_item(parent['parent'])
        return lists


if __name__ == '__main__':

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
    ts = TreeStore(items)

    assert ts.get_item(7) == {'id': 7, 'parent': 4, 'type': None}

    assert ts.get_children(4) == [
        {'id': 7, 'parent': 4, 'type': None},
        {'id': 8, 'parent': 4, 'type': None}
    ]

    assert ts.get_all_parents(7) == [
        {'id': 4, 'parent': 2, 'type': 'test'},
        {'id': 2, 'parent': 1, 'type': 'test'},
        {'id': 1, 'parent': 'root'}
    ]

    print('Test successfully retrieved')
