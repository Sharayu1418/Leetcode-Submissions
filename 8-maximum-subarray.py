class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both with the first element.
        # (This handles arrays that have all negative numbers)
        current_sum = nums[0]
        max_sum = nums[0]

        # Start loop from 2nd element since we already used the first one
        for i in range(1, len(nums)):

           
            # Decide whether to:
            # start a new subarray from current element
            # Or extend the previous subarray
            # Example: if current_sum was negative, starting fresh gives a higher sum.
            current_sum = max(nums[i], current_sum + nums[i])

            # Update max_sum only AFTER updating current_sum.
            # Because current_sum represents the best subarray sum *ending at index i*.
            max_sum = max(max_sum, current_sum)

        # Return the overall maximum subarray sum found
        return max_sum
