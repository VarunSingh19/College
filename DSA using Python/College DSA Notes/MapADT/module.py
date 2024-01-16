class Map:
    def __init__(self):
        self.map = {}
    
    def get(self,key):
        return self.map.get(key)
    
    def set(self,key,value):
        self.map[key] = value
    
    def delete(self,key):
        del self.map[key]
    
    def contains(self,key):
        return key in self.map

    def size(self):
        return len(self.map)
    
    def keys(self):
        return list(self.map.keys())
    
    def values(self):
        return list(self.map.values())
    
    def items(self):
        return list(self.map.items())
    
    def clear(self):
        self.map = {}
    

map_obj = Map()
map_obj.set("Apple",1)
map_obj.set("Banana",5)
map_obj.set("Mango",2)
map_obj.set("Watermelon",4)

print(map_obj.get("Apple"))
print(map_obj.contains("Banana"))
print(map_obj.contains("Orange"))
print(map_obj.contains("Mango"))

map_obj.delete("Mango")
print(map_obj.keys())

map_obj.clear()
print(map_obj.size())




