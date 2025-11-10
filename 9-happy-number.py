class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # to track numbers we've already seen (detect loops)

        while n != 1:
            if n in seen:  # if we see the same number again, it’s looping
                return False
            seen.add(n)

            # break number into digits, square each, and sum
            n = sum(int(digit) ** 2 for digit in str(n))

        # if we reach 1, it’s a happy number
        return True
