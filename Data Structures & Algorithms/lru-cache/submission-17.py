class Node:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashtable = {}
        self.right = Node(None, None)
        self.left = Node(None, None)
        self.capacity = capacity
        
        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToHead(self, node):
        oldHead = self.right.prev

        oldHead.next = node
        node.prev = oldHead

        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key not in self.hashtable:
            return -1
        
        else:
            node = self.hashtable[key]
            self.remove(node)
            self.addToHead(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashtable:
            self.hashtable[key].val = value
            self.remove(self.hashtable[key])
        else:
            self.hashtable[key] = Node(key, value)
        
        self.addToHead(self.hashtable[key])

        if len(self.hashtable) > self.capacity:
            lru = self.left.next

            self.remove(lru)

            self.hashtable.pop(lru.key)


        
