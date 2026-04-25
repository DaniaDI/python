class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        index = self.hash(key)
        pairs = self.map[index]

        for i, (k, v) in enumerate(pairs):
            if k == key:
                pairs[i] = (key, value)  
                return

        pairs.append((key, value))  

    def get(self, key):
        index = self.hash(key)
        pairs = self.map[index]

        for k, v in pairs:
            if k == key:
                return v

        return -1

    def remove(self, key):
        index = self.hash(key)
        pairs = self.map[index]

        for i, (k, v) in enumerate(pairs):
            if k == key:
                pairs.pop(i)
                return
# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1001, 1)
param_2 = obj.get(1001)
obj.remove(1001)


my_hash_map = MyHashMap()

# Insert data
my_hash_map.put(1, 100)
my_hash_map.put(1001, 200) # Index collision with key 1, handled via chaining

# Retrieve data
print(my_hash_map.get(1))    # Output: 100
print(my_hash_map.get(1001)) # Output: 200

# Remove data
my_hash_map.remove(1)
print(my_hash_map.get(1))    # Output: -1 (Not found)
print(my_hash_map.get(1001)) # Output: 200 (Still exists)

 