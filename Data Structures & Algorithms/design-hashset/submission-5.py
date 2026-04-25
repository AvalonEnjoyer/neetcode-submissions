class MyHashSet:
    def __init__(self, size=1000):
        self.size = size
        self.hashset = [[] for _ in range(size)]

    def add(self, key: int) -> None:
        key_hash =  hash(key)
        bucket = key_hash % len(self.hashset)
        if [key_hash, key] in self.hashset[bucket]:
            return
        else:
            self.hashset[bucket].append([key_hash,key])

    def remove(self, key: int) -> None:
        key_hash = hash(key)
        bucket = key_hash % len(self.hashset)
        if [key_hash, key] in self.hashset[bucket]:
            self.hashset[bucket].remove([key_hash,key])

    def contains(self, key: int) -> bool:
        key_hash = hash(key)
        bucket = key_hash % len(self.hashset)
        return True if [key_hash,key] in self.hashset[bucket] else False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)