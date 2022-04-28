class Solution:
    # Presum array of cost[i] - gas[i]
    #    gas = [1, 2, 3, 4, 5]
    #   cost = [3, 4, 5, 1, 2]
    # presum = [2, 4, 6, 3, 0]
    # if sum(gas) < sum(cost), impossible
    # Need to choose a starting point, such that all the elements of the
    # presum array starting at that point are all non-negative. To do so,
    # we just need to find the max(presum)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        presum = 0
        maxi_idx, maxi = 0, cost[0] - gas[0]
        for i in range(len(gas)):
            curr = cost[i] - gas[i]
            presum += curr
            if presum > maxi:
                maxi = presum
                maxi_idx = i
        return (maxi_idx + 1) % len(gas)