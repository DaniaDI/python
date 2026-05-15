class ListNode:
    def __init__(self, key=-1, value=-1 ):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.map = [ListNode() for i in range(self.size)]

    def hash(self, key):
        return key % len(self.map)
    
    def put(self, key:int, value:int) -> None:
        index = self.map[self.hash(key)]
        while index.next:
            index = index.next
            if index.key == key:
                index.value = value
                return

        index.next = ListNode(key, value)

    def get(self, key:int) -> int:
      index = self.map[self.hash(key)].next
      while index.next:
            if index.key == key:
                return index.value
            index = index.next
      return -1

    def remove(self, key:int) -> None:
        index = self.hash(key)
        pairs = self.map[index]

        for i, (k, v) in enumerate(pairs):
            if k == key:
                pairs.pop(i)
                return