class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashtable = {}
        self.tail, self.head = None, None

    def get(self, key: int) -> int:
        if key not in self.hashtable:
            return -1
        
        node = self.hashtable[key]

        if node == self.head:
            return node.val
        
        if node == self.tail:
            self.tail = self.tail.next
            self.tail.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self.head.next = node
        node.prev = self.head
        node.next = None
        self.head = node

        return node.val 

    def put(self, key: int, value: int) -> None:
        if key in self.hashtable:
            node = self.hashtable[key]

            if node != self.head:
                if node == self.tail:
                    self.tail = self.tail.next
                    self.tail.prev = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                
                self.head.next = node
                node.prev = self.head
                node.next = None
                self.head = node

            node.val = value
        else:
            if self.capacity == 1 and len(self.hashtable) == 1:
                self.hashtable.pop(self.tail.key)
                self.tail = self.head = Node(key, value, None, None)
                self.hashtable[key] = self.head
            elif len(self.hashtable) == 0:
                self.tail = self.head = Node(key, value, None, None)
                self.hashtable[key] = self.head
            
            elif len(self.hashtable) >= self.capacity:
                self.hashtable.pop(self.tail.key)
                self.tail = self.tail.next
                self.tail.prev = None
                

                self.head.next = Node(key, value, None, self.head)
                self.head = self.head.next
                self.hashtable[key] = self.head
            else:
                self.head.next = Node(key, value, None, self.head)
                self.head = self.head.next
                self.hashtable[key] = self.head

    
