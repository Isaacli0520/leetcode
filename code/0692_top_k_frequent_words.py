class Solution:
    # Time: O(nlogk)
    # Space: O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        hp = []
        for word, freq in c.items():
            heapq.heappush(hp, Word(word, freq))
            if len(hp) > k:
                heapq.heappop(hp)
        
        res = []
        while hp:
            res.append(heapq.heappop(hp).word)
        return res[::-1]
        
class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return other.word < self.word
        
        