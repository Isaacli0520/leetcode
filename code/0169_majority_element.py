class Solution:
    # O(1) space complexity
    # Since the majority element appears more than n/2 times, 
    # It must be the major element that has a count > 0 in the end
    #
    # Since we subtract 1 if curr element is not equal to major,
    # worst case is when we pair every non-major element with the 
    # major element. Since it appears more than n/2 times, there must
    # still be one major element left, and it will make the count > 0
    # 3311112
    # 3131211
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            # Mark current as new majority
            if cnt == 0:
                major = nums[i]
            
            if major == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return major
        
    
    # O(n) space complexity
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        l = len(nums) // 2
        for num in nums:
            d[num] += 1
            if d[num] > l:
                return num