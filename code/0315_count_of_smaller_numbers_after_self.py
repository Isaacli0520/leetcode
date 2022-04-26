class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        def helper(ls):
            if len(ls) <= 1:
                return ls
            mid = len(ls) // 2
            left = helper(ls[:mid])
            right = helper(ls[mid:])
            l, r = len(left) - 1, len(right) - 1
            for i in range(len(ls) - 1, -1, -1):
                if r < 0 or (l >= 0 and nums[left[l]] > nums[right[r]]):
                    res[left[l]] += r + 1
                    ls[i] = left[l]
                    l -= 1
                else:
                    ls[i] = right[r]
                    r -= 1
            return ls
        
        helper(list(range(len(nums))))
        return res

    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        def sort(indexes):
            if len(indexes) <= 1:
                return indexes
            mid = len(indexes) // 2
            left = sort(indexes[:mid])
            right = sort(indexes[mid:])
            for i in range(len(indexes) - 1, -1, -1):
                # Start from the biggest
                # nums[left[-1]] is bigger than every index in right, so we 
                # increment the res[left[-1]] by len(right)
                if not right or (left and nums[left[-1]] > nums[right[-1]]):
                    # Keep track of indices to ensure the correct index
                    # of the element is selected
                    res[left[-1]] += len(right)
                    indexes[i] = left.pop()
                else:
                    indexes[i] = right.pop()
            return indexes
        sort(list(range(len(nums))))
        return res