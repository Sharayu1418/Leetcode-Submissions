class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}  

        for ch in s:
            # if it's an opening bracket, push it
            if ch in mapping:
                stack.append(ch)
            else:
                # if it's a closing bracket, stack must not be empty
                if not stack:
                    return False
                top = stack.pop()
                # check if this closing bracket matches the expected one
                if mapping[top] != ch:
                    return False

        # return True if stack is empty (all brackets matched), else False
        return not stack  # same as:
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False









        