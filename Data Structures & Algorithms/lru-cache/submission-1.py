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
        self.size = 0
        self.capacity = capacity
        self.head.next, self.end.prev = self.end, self.head

    def get(self, key: int) -> int:
        search_res = self.hashmap.get(key, None)
        if search_res == None:
            return -1
        # Update the cache position
        # Detach cur from existing linked list
        curr = search_res
        curr.prev.next, curr.next.prev = curr.next, curr.prev
        curr.next, curr.prev = self.end, self.end.prev
        self.end.prev.next = curr
        self.end.prev = curr
        return search_res.val
        
    def put(self, key: int, value: int) -> None:
        # Update if it exists
        if self.hashmap.get(key, None) != None:
            curr = self.hashmap[key]
            self.hashmap[key].val = value 
            # Detach cur from existing linked list
            curr.prev.next, curr.next.prev = curr.next, curr.prev
        else:
            self.size += 1
            # Create new one
            curr = Node(key, value)
            self.hashmap[key] = curr

        # Update the cache position of curr
        curr.next, curr.prev = self.end, self.end.prev
        self.end.prev.next = curr
        self.end.prev = curr
        
        # Delete if greater than capacity
        if self.size > self.capacity:
            to_delete = self.head.next.key
            # Remove the linked list connections
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            # Delete the entry from the dictionary
            self.hashmap.pop(to_delete, None)
            self.size-=1
        print(self.hashmap.items())
        
        
        
    # def get_node(self, key) -> Node:

            
    # def push_node(self, node) -> None:

