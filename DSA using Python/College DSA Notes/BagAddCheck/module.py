# Write a Program to add and check the book in the bag. 
def Bag_Question():
    class Bag:
        def __init__(self):
            self.theitems = []
        def add(self,item):
            self.theitems.append(item)
            # print(self.theitems)

        def check(self,value):
            if value in self.theitems:
                print("the Bag Contains the Value : ", value)
            else:
                print("the Bag doest have the value : ", value)
    Mybag = Bag()
    Mybag.add(19)
    Mybag.add(2)
    Mybag.add(23)
    Mybag.add(19)
    Mybag.add(12)
    Mybag.check(19)
Bag_Question()
