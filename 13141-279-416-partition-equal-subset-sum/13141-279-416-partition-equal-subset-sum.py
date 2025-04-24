from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        
        # If the total sum is odd, it's impossible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        # We need to find a subset whose sum is half of the total sum
        target = total_sum // 2
        
        # Initialize a DP array where dp[i] means if a sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True  # We can always achieve a sum of 0 (by taking no elements)
        
        # Iterate through each number in the input array
        for num in nums:
            # Traverse backwards to prevent overwriting results of the same iteration
            for j in range(target, num - 1, -1):
                # If we can achieve the sum j-num, then we can achieve sum j by adding num
                dp[j] = dp[j] or dp[j - num]
        
        #The result is whether we can achieve the target sum
        return dp[target]
