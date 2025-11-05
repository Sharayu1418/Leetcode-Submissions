class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            result.append(prod)
        
        return result
