class HashItem:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [ None for i in range(self.size)]  # total slots
        self.count = 0   # Filled slots

    def _hash(self,key):
        multiplier = 1
        hash_value = 0
        for ch in key:
            hash_value += multiplier * ord(ch)
            multiplier += 1
        return hash_value % self.size
    
    def put(self,key,value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h+1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
        
    def get(self,key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h+1) % self.size
        return None
    
def hash(name,age,sex):
    sum = 0
    for ch in name:
        sum +=ord(ch) % age
    sum += ord(sex)
    return sum % 6

print(hash("staphone", 20, "M"))