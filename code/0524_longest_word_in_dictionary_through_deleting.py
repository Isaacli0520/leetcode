class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        d = sorted(dictionary, key=lambda x:(-len(x), x))
        for word in d:
            l = 0
            for c in s:
                if l < len(word) and c == word[l]:
                    l += 1
            if l == len(word):
                return word
        return ""
        