from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []  
        #If s is shorter than p, no anagrams can exist.
        if len(s) < len(p):
            return result
        p_count = [0] * 26
        s_count = [0] * 26
        for char in p:
            p_count[ord(char) - ord('a')] += 1
        window_length = len(p)
        for i in range(window_length):
            s_count[ord(s[i]) - ord('a')] += 1
        if s_count == p_count:
            result.append(0)
        for i in range(window_length, len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - window_length]) - ord('a')] -= 1
            if s_count == p_count:
                result.append(i - window_length + 1)
        
        return result
