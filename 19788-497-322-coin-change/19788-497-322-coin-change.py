from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a dp array with values initialized to infinity (or a large number)
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 amount requires 0 coins
        dp[0] = 0
        
        # Iterate over all coin denominations
        for coin in coins:
            # Update dp array for each possible amount that can be achieved
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, return -1 (impossible to make the amount)
        return dp[amount] if dp[amount] != float('inf') else -1

        