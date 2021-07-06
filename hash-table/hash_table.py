#!/usr/bin/env python3

class HashTable:
    def __init__(self, size):
        self.table = []
        for i in range(size):
            self.table.append([])


    def set(self, key, value):
        address = self._hash(key)
        self.table[address].append([key, value])
        return self


    def get(self, key):
        address = self._hash(key)

        bucket = self.table[address]

        if not bucket: return

        for item in bucket:
            if key == item[0]:
                return item[1]
        return


    def remove(self, key):
        address = self._hash(key)

        bucket = self.table[address]

        if not bucket: return

        for index, item in enumerate(bucket):
            if key == item[0]:
                bucket.pop(index)
                return


    # Generage a number between [0..size]
    def _hash(self, key):
        hash = 0

        for index, item in enumerate(str(key)):
            hash = (hash + ord(item) * (index + 1)) % len(self.table)

        return hash


    def display(self):
        for bucket in self.table:
            if bucket:
                for item in bucket:
                    print(f"{item[0]}: {item[1]}")


if __name__ == "__main__":

    ht = HashTable(20)

    ht.set("apple", 10)
    ht.set("orange", 5)
    ht.set("grape", 200)
    ht.set("pineapple", 3)
    ht.get("apple") # return 10
    ht.remove("pineapple")

    ht.display()
