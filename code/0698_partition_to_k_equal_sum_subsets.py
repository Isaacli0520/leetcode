class Solution:
    # Backtracking
    # For each number, try put it in any bucket
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        if tot % k != 0:
            return False
        
        # Start from big nums
        nums = sorted(nums, reverse=True)
        l = len(nums)
        target = tot // k
        buck = [0] * k
        
        # Try placing nums[idx] in any bucket
        def helper(idx):
            if idx == l:
                return buck[0] == target and len(set(buck)) == 1
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= target and helper(idx + 1):
                    return True
                buck[i] -= nums[idx]
                
                # If you tried to put a number in an empty bucket
                # and it did not work, putting it in other buckets
                # won't work either
                # *Key line to reduce runtime
                if buck[i] == 0:
                    break
            return False
        
        return helper(0)
                    
                
                    