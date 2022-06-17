class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # Time: O(n); n = length of word
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.val = word

    # Time: Worst O(M); M = total number of nodes in Trie
    def search(self, word: str) -> bool:
        n = len(word)
        
        def helper(curr, idx):
            if idx == n:
                return curr.val is not None
            if word[idx] == ".":
                return any(helper(child, idx + 1) for child in curr.children.values())
            
            if word[idx] in curr.children:
                return helper(curr.children[word[idx]], idx + 1)
            return False
        
        return helper(self.root, 0)
            
        
class TrieNode():
    def __init__(self):
        self.val = None
        self.children = {}
        
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)