class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Build a frequency dictionary
        # Key- number from the array
        # Value- how many times that number appears
        freq = {}
        for n in nums:
            # freq.get(n, 0) returns current count of n, or 0 if n is not seen before
            freq[n] = freq.get(n, 0) + 1
        
        # Sort the numbers based on their frequency (highest first)
        # sorted(freq) sorts the dictionary keys
        # key=lambda x: freq[x] means: sort keys by their frequency value
        # reverse=True means: highest frequency comes first
        sorted_nums = sorted(freq, key=lambda x: freq[x], reverse=True)
        
        # Take the first k elements from the sorted list
        # slice the first k most frequent numbers
        return sorted_nums[:k]
