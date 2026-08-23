class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.head = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashtable = {}

        self.left = Node(None, None)
        self.right = Node(None, None)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToHead(self, node):
        oldHead = self.right.prev

        oldHead.next = node
        node.prev = oldHead

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashtable:
            return -1
        
        node = self.hashtable[key]

        self.remove(node)
        self.addToHead(node)

        return node.val 


    def put(self, key: int, value: int) -> None:
        if key in self.hashtable:
            node = self.hashtable[key]

            node.val = value
            self.remove(node)
            self.addToHead(node)
        
        else:
            node = Node(key, value)

            self.hashtable[key] = node
            self.addToHead(node)

            if len(self.hashtable) > self.capacity:
                lru = self.left.next

                self.remove(lru)
                self.hashtable.pop(lru.key)
        

    
