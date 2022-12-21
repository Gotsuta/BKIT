#from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = list(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.unique_items = set()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.items) == 0:
            raise StopIteration
        item = self.items.pop(0)
        if self.ignore_case:
            item = item.lower()
        if item not in self.unique_items:
            self.unique_items.add(item)
            return item
        else:
            return self.__next__()
        

# data = [1,1,1,2,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
# print(*Unique(data))
# data = ['a', 'A', 'B', 'a', 'b']
# print(*Unique(data, ignore_case=True))
# print(*Unique(data))