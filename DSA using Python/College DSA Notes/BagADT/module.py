class Bag:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def remove(self,item):
        if item in self.items:
            self.items.remove(item)
    
    def count(self,item):
        return self.items.count(item)

    def contains(self,item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)
    def size(self):
        return len(self.items)
    def show(self):
        print(self.items)
    
bag = Bag()
bag.add(10)
bag.add(233)
bag.add(43)
bag.add(54)
bag.add(10)
print("Size:", bag.size())
print("Contains 10:" , bag.contains(10))
print("Count 10:" , bag.count(10))
bag.remove(10)
print("Count of 10 after removel :" , bag.count(10))
bag.show()