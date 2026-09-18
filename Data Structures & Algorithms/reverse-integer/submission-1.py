class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:

            return 0
        
        if x > 0:

            num = []

            while x:

                rem = x % 10

                num.append(rem)

                x = x // 10
            
            ans = int("".join(map(str,num)))

            if not (-(2**31) <= ans <= (2**31 - 1)):

                return 0
            else:

                return ans


        else:

            x = abs(x)

            num = []

            while x:

                rem = x % 10

                num.append(rem)

                x = x // 10
            
            ans = - int("".join(map(str,num)))

            if not (-(2**31) <= ans <= (2**31 - 1)):

                return 0
            else:

                return ans
        



