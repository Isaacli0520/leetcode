class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.d) == self.cap:
                node = self.head.next
                self.remove(node)
                del self.d[node.key]
            node = Node(key, value)
            self.add(node)
            self.d[key] = node
        return None
        
    def remove(self, node):
        tmp = node.prev
        node.prev.next = node.next
        node.next.prev = tmp
        # node.prev.next, node.next.prev = node.next, node.prev
        
    # Add at tail
    def add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        
    # def printList(self):
    #     curr = self.head
    #     res = []
    #     while curr is not None:
    #         res.append(str(curr.val))
    #         curr = curr.next
    #     print(" ".join(res))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)