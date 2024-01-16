class Bag:
    def __init__(self):
        self.items = []
    def add(self,item):
        return self.items.append(item)
    def remove(self,item):
        if item in self.items:
            self.items.remove(item)
    def count(self,item):
        return self.items.count(item)
    def size(self):
        return len(self.items)
    def contains(self,item):
        return item in self.items    
    def __iter__(self):
        return iter(self.items)
    def show(self):
        print(self.items)

bag = Bag()
bag.add(2)
bag.add(44)
bag.add(54)
bag.add(4)
print("Removed item :",bag.remove(4))
bag.show()
print("the bag contains :",bag.contains(21))
print("The Size :", bag.size())        
    