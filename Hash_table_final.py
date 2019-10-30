class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def my_hashing(self, key):
        if type(key) is int:
            return key % 10  # This is the number between 0 and 9, and is going to be used
            # as the index to assign the value
        else:
            for i in key:
                total_ascii = 0
                total_ascii += ord(i)
        return total_ascii % self.size

    def insertation(self, key, value):
        hashkey = self.my_hashing(key)
        keyvalue = [key, value]
        if self.table[hashkey] is None:  # if the key does not exist simply add the key and value
            self.table[hashkey] = list([keyvalue])
        else:
            for e in self.table[hashkey]:
                if e[0] == key:  # if the key exist just update the value
                    e[1] = value
            self.table[hashkey].append(keyvalue)

    def get_value(self, key):
        hashkey = self.my_hashing(key)
        if self.table[hashkey] is None:
            return "no such key exist"
        else:
            for d in self.table[hashkey]:
                if d[0] == key:
                    return d[1]

    def delete_value(self,key):
        hashkey = self.my_hashing(key)
        if self.table[hashkey] is None:
            return "please enter valid key"
        else:
            for h in self.table[hashkey]:
                if h[0] == key:
                    del(h[1])
                    del(h[0])

    def print_table(self):
        print("Hash Table")
        for item in self.table:
            if item is not None:
                print(item)
            else:
                pass


h = HashTable(8)
h.insertation("MMMMMM", "1")
h.insertation("GGGGGGGGG", "99999")
h.insertation("K", "000000000000000000000000")
h.insertation(2,"int")
h.print_table()
h.delete_value("K")
h.print_table()

