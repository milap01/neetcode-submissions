class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for oper in operations:

            if oper == "+" and len(stack) >= 2:

                su = int(stack[-1]) + int(stack[-2])
                stack.append(su)
            elif oper == "D" and len(stack) >= 1:

                num = 2 * int(stack[-1])
                stack.append(num)
            elif oper == "C" and len(stack) != 0:

                stack.pop()
            else:

                stack.append(int(oper))
        
        cur = 0

        print(stack)

        for num in stack:

            cur += num
        
        return cur



        