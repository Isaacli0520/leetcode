class Solution:
    # DP Optimized with Trie
    # Time: O(N^2 + T) | O(N^2) for building DP; O(T) for building trie
    # Space: O(N + T)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        trie = TrieNode()
        for word in wordDict:
            trie.insert(word)
        
        # dp[i] = whether s[i:] can be segmented into dict words
        dp = [False] * (n + 1)
        dp[n] = True
        for start in range(n - 1, -1, -1):
            curr = trie
            for end in range(start + 1, n + 1):
                c = s[end - 1]
                
                # s[start:end] not in trie
                if c not in curr.children:
                    break
                    
                curr = curr.children[c]
                if curr.val is not None and dp[end]:
                    # s[start:end] can be segmented
                    dp[start] = True
                    break
        return dp[0]
    
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
    

    
class Solution:
    # DP Time: O(N^3 + M) Space: O(N + M); M is the length of wordDict
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = { n: True }
        words = set(wordDict)
        
        def helper(start):
            if start in dp:
                return dp[start]
            
            # O(N^2)
            for end in range(start + 1, n + 1):
                word = s[start:end] # O(N)
                if word in words and helper(end):
                    dp[start] = True
                    return True
            dp[start] = False
            return False
            
        return helper(0)