# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Adrianna Gilmore


class HashTable:

    def __init__(self, size = 10):
        self.size = size
        self.data = [] 
        for i in range(self.size):
            self.data.append([])
            i += 1

    def hash(self, key):
        return hash(key) % len(self.data)
    
    def __setitem__(self, key, value):
        self.miniList = self.data[self.hash(key)]
        if self.isEmpty(self.miniList) == False:
            if self.miniList[0] == key:
                self.newList = [key, value]
                return self.newList
        else:
            self.miniList.append([key, value])
            return self.miniList
    
    def __getitem__(self, key):
        self.index = self.hash(key)
        self.miniList = self.data[self.index]
        if self.index >= 0 and self.index <= len(self.data):
            if self.isEmpty(self.miniList):
                return None
            else: 
                return self.miniList[0][1]
        else:
            return None

    def isEmpty(self, list):
        if len(list) == 0:
            return True
        else:
            return False




