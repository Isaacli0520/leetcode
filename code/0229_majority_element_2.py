class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m1, m2 = None, None
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == m1:
                cnt1 += 1
            elif n == m2:
                cnt2 += 1
            elif cnt1 == 0:
                m1, cnt1 = n, 1
            elif cnt2 == 0:
                m2, cnt2 = n, 1
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        res = []
        if nums.count(m1) > len(nums) // 3:
            res.append(m1)
        if nums.count(m2) > len(nums) // 3:
            res.append(m2)
        return res