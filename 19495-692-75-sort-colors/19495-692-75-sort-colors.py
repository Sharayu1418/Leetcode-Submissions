class Solution:
    def sortColors(self, nums: list[int]) -> None:
        next_red_pointer = 0           
        current = 0          
        next_blue_pointer = len(nums) - 1 
        
        while current <= next_blue_pointer:
            if nums[current] == 0:       
                nums[current], nums[next_red_pointer] = nums[next_red_pointer], nums[current]
                next_red_pointer += 1
                current += 1
            elif nums[current] == 1:     
                current += 1
            else:                        
                nums[current], nums[next_blue_pointer] = nums[next_blue_pointer], nums[current]
                next_blue_pointer -= 1
