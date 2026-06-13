class Node:

    def __init__(self, key:int, value:int):
        self.key, self.val = key, value 
        self.prev = self.next = None
        self.freq = 1

class LinkedList:

    def __init__(self):
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0

    def length(self):
        return self.size

    def push(self, node:Node) -> None:
        # Insertion always happens to the right - LRU 
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1
    
    def pop(self, node:Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.prev = node.next = None
        self.size -= 1

    def pop_left(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfu_freq = 0 
        self.node_map = {} # key -> node
        self.freq_map = defaultdict(LinkedList) # freq -> linkedlist of nodes
    
    def counter(self, node):
        freq = node.freq
        self.freq_map[freq].pop(node)

        if freq == self.lfu_freq and self.freq_map[freq].length() == 0:
            self.lfu_freq += 1
        
        node.freq += 1
        self.freq_map[node.freq].push(node)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.counter(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        # No cap
        if self.cap == 0:
            return
        
        # Existing
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.counter(node)
            return 
        
        # If capped out , delete lfu node (lru, if multiple)
        if len(self.node_map) == self.cap:
            # remove the leftmost (lru) node from lfu frequency bin
            node = self.freq_map[self.lfu_freq].pop_left()
            # remove the node from the node_map
            self.node_map.pop(node.key)

        # New entry
        node = Node(key, value)
        self.freq_map[1].push(node)
        self.node_map[key] = node
        self.lfu_freq = 1
        
    

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)