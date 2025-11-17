class Solution:
    def twoSum(self, nums, target):
        # Create (value, index) pairs
        #paired = [(value, index) for index, value in enumerate(nums)]
        paired = []
        for i in range(len(nums)):
            paired.append((nums[i], i))

        # Sort by the values
        paired.sort()

        left = 0
        right = len(paired) - 1

        # Two-pointer scan
        while left < right:
            left_val, left_idx = paired[left]
            right_val, right_idx = paired[right]

            total = left_val + right_val

            if total == target:
                return [left_idx, right_idx]

            elif total < target:
                left += 1
            else:
                right -= 1

#class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(len(nums)):
         #for j in range (i+1, len(nums)):
             #if  nums[i] + nums[j] == target:
                 #return [i,j]

    #def twoSum(self, nums, target):
        #notebook = {}   # hash map

        #for i, num in enumerate(nums):   # go through each number
            #remaining = target - num          # the number we need

            # check if we already saw the number we need
            #if remaining in notebook:
                #return [notebook[remaining], i]   # found the answer

            # if not, write the current number in the notebook
            #notebook[num] = i

        
        #return []

        