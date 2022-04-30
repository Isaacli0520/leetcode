class Solution:
    # Assume i connnects to nums[i]
    # nums = [1, 3, 4, 2, 2]
    # 0 -> 3 -> 2 -> 4 -> 4
    # Then this problem becomes finding cycles in a linked list
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow