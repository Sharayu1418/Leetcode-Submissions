class Solution:
    def reverseWords(self, s: str) -> str:
        #Split the input string into words, removing extra spaces automatically.
        words = s.split()
        #Reverse the list of words.
        words.reverse()
        #Join the reversed words with a single space and return the result.
        return " ".join(words)

        