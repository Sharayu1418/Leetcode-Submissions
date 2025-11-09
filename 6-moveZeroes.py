class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0  # slow pointer starts at 0

        for i in range(len(nums)):  # fast pointer
            if nums[i] != 0:        # found a non-zero
                nums[j] = nums[i]   # move to slow pointer position
                j += 1              # move slow pointer forward

        # fill remaining elements with zeros
        for k in range(j, len(nums)):
            nums[k] = 0