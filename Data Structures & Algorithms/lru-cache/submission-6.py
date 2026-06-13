class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = self.end = Node(-1, -1)
        # self.end = Node(-1, -1)
        self.capacity = capacity
        self.head.next, self.end.prev = self.end, self.head

    def get(self, key: int) -> int:
        search_res = self.hashmap.get(key, None)
        if search_res == None:
            return -1
        # Update the cache position
        self.remove(search_res)
        self.insert(search_res)
        return search_res.val
        
    def put(self, key: int, value: int) -> None:
        if self.hashmap.get(key, None) != None:
            self.remove(self.hashmap[key])

        curr = Node(key, value)
        self.hashmap[key] = curr
        self.insert(curr)

        # Delete if greater than capacity
        if len(self.hashmap) > self.capacity:
            to_delete = self.head.next
            # Remove the linked list connections
            self.remove(to_delete)
            # Delete the entry from the dictionary
            del self.hashmap[to_delete.key]
    
    def remove(self, node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def insert(self, node) -> None:
        node.prev, node.next = self.end.prev, self.end
        self.end.prev.next = self.end.prev = node
        
