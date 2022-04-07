import random
class Solution:
    # Example: n = 7, blacklist = [2, 3, 5]
    # Assume there is a list, where the first n - len(blacklist) items
    # are valid indices, the last len(blacklist) indices are invalid
    # [0, 1, 2, 3, | 4, 5, 6]
    #  .  .  .  .  | x  x  x 
    # Basically, we want to replace those in the right subarray that 
    # are not blacklist indices to be replaced with those in the left
    # subarray that are blacklist indices. Like the following list
    # [0, 1, 6, 4, | 3, 5, 2]
    #  .  .  .  .  | x  x  x
    # Therefore we maintain a dict, for every left subarray item that
    # is in the blacklist, remap it to an idx in the right subarray that 
    # is not in the blacklist.
    def __init__(self, n: int, blacklist: List[int]):
        d = {i:i for i in blacklist}
        self.length = n - len(blacklist)
        right = n - 1
        for i in blacklist:
            if i < self.length:
                while right in d:
                    right -= 1
                d[i] = right
                right -= 1
        self.d = d

    def pick(self) -> int:
        tmp = random.randrange(0, self.length)
        if tmp in self.d:
            return self.d[tmp]
        return tmp


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()