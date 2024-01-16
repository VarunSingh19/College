class Bag:
    def __init__(self):
        self.theItems = []
    def add(self,item):
        self.theItems.append(item)
    def check(self,v):
        if v in self.theItems:
            print("yes its exist :", v)
        else:
            print("nope i cant find the item ", v)
    def show(self):
        print(self.theItems)

myB = Bag()
myB.add(23)
myB.add(232)
myB.check(12)
myB.show()