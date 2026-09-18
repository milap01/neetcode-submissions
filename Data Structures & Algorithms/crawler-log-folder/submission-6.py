class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []

        for log in logs:

            if log == "../" and len(stack) != 0 :

                stack.pop()
            elif log == "./":

                pass
            else:

                if log != "../":
                    stack.append(log)
        
        return len(stack)
        
            

        


        