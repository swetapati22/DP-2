"""
# Time Complexity :
- O(n), where n is the number of houses

# Space Complexity :
- O(1), in-place DP (modifying input array)

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        for i in range(len(costs) - 2, -1, -1):
            costs[i][0] += min(costs[i+1][1], costs[i+1][2])
            costs[i][1] += min(costs[i+1][0], costs[i+1][2])
            costs[i][2] += min(costs[i+1][0], costs[i+1][1])

        return min(costs[0])
