class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def get(self, key):
        index = self._hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        index = self._hash_function(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return
            prev = node
            node = node.next

    def display(self):
        for index in range(self.size):
            node = self.table[index]
            print(f"Index {index}: ", end="")
            while node:
                print(f"{node.key}:{node.value}", end=" -> ")
                node = node.next
            print("None")

# Example usage:
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("cherry", 3)
hash_table.display()
print("Value for 'banana':", hash_table.get("banana"))
hash_table.remove("apple")
hash_table.display()
