"""
# Time Complexity :
- O(amount * n), where n = number of coins

# Space Complexity :
- O(amount), using a 1D DP array

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make amount 0 — by choosing no coin

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
