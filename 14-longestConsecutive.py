class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)   # fast lookups
        longest = 0

        for n in num_set:
            # start only when it's the beginning of a sequence
            if (n - 1) not in num_set:
                current = n
                count = 1      # we found 1 number in the sequence

                # keep checking next numbers
                while (current + 1) in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest

        