class MyHashMap:
    def __init__(self, size=1000):
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key:int):
        return key % len(self.buckets)

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]
        key_not_found = True
        for i, item in enumerate(bucket):
            if item[0] == key:
                key_not_found = False
                bucket.pop(i)
                bucket.append((key,value))
                break
        if key_not_found:
            bucket.append((key,value))

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        for item in bucket:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for item in bucket:
            if item[0] == key:
                bucket.remove(item)