class HashTable:

    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    # Para utilizar la sintaxis de python de 'object[index]'
    # Standard operators
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None