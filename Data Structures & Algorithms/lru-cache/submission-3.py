class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = Node(-1, -1)
        self.end = Node(-1, -1)
        self.capacity = capacity
        self.head.next, self.end.prev = self.end, self.head

    def get(self, key: int) -> int:
        search_res = self.hashmap.get(key, None)
        if search_res == None:
            return -1
        # Update the cache position
        self.push_node(search_res)
        return search_res.val
        
    def put(self, key: int, value: int) -> None:
        # Update if it exists
        if self.hashmap.get(key, None) != None:
            curr = self.hashmap[key]
            curr.val = value 
            self.push_node(curr)
        else:
            # Create new one
            curr = Node(key, value)
            self.hashmap[key] = curr
            self.push_node(curr, new=True)

        # Delete if greater than capacity
        if len(self.hashmap)> self.capacity:
            to_delete = self.head.next.key
            # Remove the linked list connections
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            # Delete the entry from the dictionary
            self.hashmap.pop(to_delete, None)
        
    def push_node(self, curr:Node, new:bool=False) -> None:
        if not new:
            curr.prev.next, curr.next.prev = curr.next, curr.prev
        curr.next, curr.prev = self.end, self.end.prev
        self.end.prev.next = curr
        self.end.prev = curr
        
