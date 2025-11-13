class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
         for j in range (i+1, len(nums)):
             if  nums[i] + nums[j] == target:
                 return [i,j]

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

        