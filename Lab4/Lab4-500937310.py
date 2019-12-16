

class MyHashTable():
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        self.arr = [None for i in range(size)]
        self.hash1 = hash1
        self.size = size

    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the table should not be changed
        hashed_key = self.hash1(key)

        if self.arr[hashed_key] is not None:
            return False
        else:
            self.arr[hashed_key] = ValueNode(key, data)
            return True

    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist
        hashed_key = self.hash1(key)
        if key > len(self.arr):
            return None

        value = self.arr[hashed_key].data
        if value is not None and key == self.arr[hashed_key].key:
            return value
        else:
            return None

    def __len__(self):
        # Returns the number of items in the Hash Table
        counter = 0
        for value in self.arr:
            if value is not None:
                counter = counter + 1

        return counter


    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        for value in self.arr:
            if value is None:
                return False

        return True

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        super().__init__(size,hash1)

    def put(self, key, data):
        hashed_key = self.hash1(key)

        if self.arr[hashed_key]:
            self.arr[hashed_key].append(ValueNode(key, data))
            return True
        else:
            self.arr[hashed_key] = [ValueNode(key, data)]
            return True

    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist
        hashed_key = self.hash1(key)
        if self.arr[hashed_key]:
            for valueNode in self.arr[hashed_key]:
                if valueNode.key == key:
                    return valueNode.data
        else:
            return None
        pass

    def __len__(self):
        # Returns the number of items in the Hash Table
        counter = 0;
        for item in self.arr:
            if item:
                for i in item:
                    counter = counter + 1
            else:
                continue
        return counter

    def isFull(self):
        return False

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        super().__init__(size,hash1)
        self.hash2 = hash2

    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the key should be rehashed using some combination of the first and second hash functions
        # Be careful that your code does not enter an infinite loop
        if self.isFull():
            return False

        idx = self.hash1(key)

        if self.arr[idx]:
            idx2 = self.hash2(key)
            i = 1
            usedIdxs = []
            newIdx = 0
            while (True):
                newIdx = (idx + i * idx2) % len(self.arr)
                if newIdx in usedIdxs:
                    return False

                if not self.arr[newIdx]:
                    self.arr[newIdx] = ValueNode(key, data)
                    return True

                i = i + 1
        else:
            self.arr[idx] = ValueNode(key, data)
            return True

    def get(self, key):
        idx = self.hash1(key)

        if self.arr[idx] and self.arr[idx].key == key:
            return self.arr[self.hash1(key)].data
        else:
             idx2 = self.hash2(key)
             i = 1
             usedIdxs = []
             newIdx = 0
             while (True):
                newIdx = (idx + i * idx2) % len(self.arr)
                if newIdx in usedIdxs:
                     return None

                if self.arr[newIdx] and self.arr[newIdx].key == key:
                    return self.arr[newIdx].data

                i = i + 1



    def __len__(self):
        counter = 0
        for value in self.arr:
            if value:
                counter = counter + 1

        return counter

class ValueNode():
    def __init__(self, key, data):
        self.key = key
        self.data = data





