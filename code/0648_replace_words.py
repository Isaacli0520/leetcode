class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieNode()
        for word in dictionary:
            trie.insert(word)
        
        res = []
        for word in sentence.split():
            root = trie.findRoot(word)
            if root is not None:
                res.append(root)
            else:
                res.append(word)
        return " ".join(res)
        
class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}
        
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.val = word
    
    def findRoot(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                return None
            curr = curr.children[c]
            if curr.val is not None:
                return curr.val
        return None