class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.d = {}

    # Update prefixes on path by delta
    def insert(self, key: str, val: int) -> None:
        delta = val - self.d.get(key, 0)
        self.d[key] = val
        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.val += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.val
        
class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = {}


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)