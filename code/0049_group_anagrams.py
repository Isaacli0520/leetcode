class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
            
        for s in strs:
            code = "".join(sorted(s))
            d[code].append(s)
        
        return list(d.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        
        def helper(s):
            cnt = Counter(s)
            key = [0] * 26
            for c, v in cnt.items():
                key[ord(c) - 97] = v
            return tuple(key)
            
        for s in strs:
            code = helper(s)
            d[code].append(s)
        
        return list(d.values())