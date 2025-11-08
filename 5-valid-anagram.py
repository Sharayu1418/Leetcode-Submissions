# O(n^2) Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        for char in t:
            if char in s_list:
                s_list.remove(char)
            else:
                return False
        return len(s_list) == 0
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # No need to sort if they’re not even the same size.
        if len(s) != len(t):
            return False

        # Sort both strings alphabetically.
        # sorted() turns them into lists of characters like ['a', 'a', 'g', 'm', 'n', 'r']
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        # Compare the sorted versions directly.
        # If every character appears in the same position after sorting → they’re anagrams.
        return sorted_s == sorted_t



# O(n) Solution
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths are different, they can’t be anagrams.
        if len(s) != len(t):
            return False

        # Create an empty dictionary (hash map) to keep track of letter counts.
        count = {}

        # Loop through string s and count each character.
        for char in s:
            # If the character already exists in the dictionary → add 1 to its count.
            # If it's new start with count 1.
            # The get(char, 0) means: "get the current count if it exists, else use 0."
            count[char] = count.get(char, 0) + 1

        for char in t:
            # If the letter in t doesn’t exist in our count dictionary,
            # it means t has a character that s never had → not an anagram.
            if char not in count:
                return False

            # Subtract 1 from that character’s count → one occurrence is used up.
            count[char] -= 1

            # If the count ever drops below 0,
            # it means t has more of this letter than s → not an anagram.
            if count[char] < 0:
                return False
        # All counts went back to zero → both words have same letters & frequencies.
        return True
