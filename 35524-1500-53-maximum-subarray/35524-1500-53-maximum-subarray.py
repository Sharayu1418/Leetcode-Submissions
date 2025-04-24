from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the current sum and the maximum sum found so far
        current_sum = nums[0]  # Start with the first element
        max_sum = nums[0]      # Start with the first element
        
        # Loop through the array starting from the second element
        for num in nums[1:]:
            # If adding the current number to the current sum is worse than starting fresh from the current number
            # Then, reset the current sum to the current number
            current_sum = max(num, current_sum + num)
            
            # Update the max_sum if we found a new maximum
            max_sum = max(max_sum, current_sum)
        
        # Return the largest sum found
        return max_sum
