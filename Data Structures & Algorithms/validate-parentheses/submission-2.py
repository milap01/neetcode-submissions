class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        opend = ['(','[','{']

        closed = [')',']','}']

        mp = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for char in s:

            if char in opend:

                stack.append(char)
            else:

                if not stack:

                    return False

                ch = stack.pop()

                if char != mp[ch]:

                    return False
        
        return True if len(stack) == 0 else False
        