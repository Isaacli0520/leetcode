class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        b_r, b_c = len(board), len(board[0])
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        for i in range(b_r):
            for j in range(b_c):
                self.dfs(board, i, j, node, "", res)
        return res
    
    def dfs(self, board, r, c, node, word, res):
        if node.isWord:
            res.append(word)
            node.isWord = False
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return
        tmp = board[r][c]
        node = node.children.get(tmp)
        if not node:
            return
        board[r][c] = "#"
        for a, b in [(r - 1, c), (r,c - 1), (r + 1, c), (r, c + 1)]:
            self.dfs(board, a, b, node, word + tmp, res)
        board[r][c] = tmp