class Solution:
    # Freq counts the nums left to be placed
    # Need counts the nums that can be placed into existing
    # len > 3 subsequences, say we have 1, 2, 3; 6, 7, 8, then
    # need = {4:1, 9:1}
    # 
    # For a new num, always put it at the end of existing subseqs
    # If not, try create a len 3 subseq with it as the starting
    # value (since the whole list is sorted).
    # If neither works, return False
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = collections.defaultdict(int)
        for num in nums:
            if freq[num] == 0:
                continue
            if num in need and need[num] > 0:
                need[num] -= 1
                freq[num] -= 1
                need[num + 1] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1
            else:
                return False
        return True
        