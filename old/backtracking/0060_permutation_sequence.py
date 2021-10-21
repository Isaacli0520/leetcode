class Solution:
    def getPermutation(self, n, k):
        nums = list(range(1, n+1))
        res = ''
        # k -= 1 is the key
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            res += str(nums[index])
            # remove from list
            nums.remove(nums[index])

        return res