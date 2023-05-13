class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def _find_next_slot(self, index):
        next_index = (index + 1) % self.size
        while self.keys[next_index] is not None:
            next_index = (next_index + 1) % self.size
        return next_index

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
        else:
            if self.keys[index] == key:
                self.values[index] = value
            else:
                next_index = self._find_next_slot(index)
                while self.keys[next_index] is not None and self.keys[next_index] != key:
                    next_index = self._find_next_slot(next_index)
                self.keys[next_index] = key
                self.values[next_index] = value

    def get(self, key):
        index = self._hash_function(key)
        if self.keys[index] == key:
            return self.values[index]
        else:
            next_index = self._find_next_slot(index)
            while self.keys[next_index] is not None and self.keys[next_index] != key:
                next_index = self._find_next_slot(next_index)
            if self.keys[next_index] == key:
                return self.values[next_index]
        return None

    def remove(self, key):
        index = self._hash_function(key)
        if self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
        else:
            next_index = self._find_next_slot(index)
            while self.keys[next_index] is not None and self.keys[next_index] != key:
                next_index = self._find_next_slot(next_index)
            if self.keys[next_index] == key:
                self.keys[next_index] = None
                self.values[next_index] = None

    def display(self):
        for index in range(self.size):
            if self.keys[index] is not None:
                print(f"Index {index}: {self.keys[index]}:{self.values[index]}")
            else:
                print(f"Index {index}: None")

# Example usage:
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("cherry", 3)
hash_table.display()
print("Value for 'banana':", hash_table.get("banana"))
hash_table.remove("apple")
hash_table.display()
