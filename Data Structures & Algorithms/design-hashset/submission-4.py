class MyHashSet:
    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        key_hash =  hash(key)
        if key_hash not in self.hashset:
            self.hashset.append(key_hash)

    def remove(self, key: int) -> None:
        key_hash = hash(key)
        if self.contains(key_hash):
            self.hashset.remove(key_hash)

    def contains(self, key: int) -> bool:
        return True if hash(key) in self.hashset else False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)