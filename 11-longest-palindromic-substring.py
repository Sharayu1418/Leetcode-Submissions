class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""   # to store the longest palindrome found
        
        # Helper function to expand from the center
        def center(left, right):
            # Expand while within bounds and characters match
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring (since loop goes one step too far)
            return s[left + 1:right]
        
        # Try every index as a potential center
        for i in range(n):
            # Odd-length palindrome (single center)
            palindrome1 = center(i, i)
            # Even-length palindrome (double center)
            palindrome2 = center(i, i + 1)
            
            # Pick the longer palindrome from the two
            longer_palindrome = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
            
            # Update longest if we found a bigger one
            if len(longer_palindrome) > len(longest):
                longest = longer_palindrome
        
        return longest
