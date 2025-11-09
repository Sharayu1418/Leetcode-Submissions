class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create an empty list to use as a queue (to hold current substring characters)
        queue = []
        max_length = 0

        # Go through each character in the string
        for c in s:
            # If the character is not already in our current substring
            if c not in queue:
                # Add it to the queue
                queue.append(c)
            else:
                # If the character is already in the queue (duplicate found)
                # Remove characters from the start (left) of the queue
                # until this duplicate character is no longer in the queue
                while c in queue:
                    queue.pop(0)
                # Now add the current character to the queue
                queue.append(c)

            # Update the maximum length if current queue is longer
            max_length = max(max_length, len(queue))

        # After checking all characters, return the longest length found
        return max_length
