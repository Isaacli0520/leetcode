class LRUCache:
    
    def __init__(self, capacity: int):
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.add_at_tail(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.remove(self.d[key])
            self.add_at_tail(node)
        else:
            if len(self.d) == self.cap:
                del self.d[self.head.next.key]
                self.remove(self.head.next)
            node = Node(key, value)
            self.d[key] = node
            self.add_at_tail(node)
                
            
    def add_at_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

class Node():
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)