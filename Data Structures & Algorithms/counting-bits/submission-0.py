class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []

        def count1(num):

            cnt = 0

            while num:

                rem = num % 2

                cnt += 1 if rem == 1 else 0

                num = num // 2
            
            return cnt

        for i in range(n+1):

            count = count1(i)

            ans.append(count)
        
        return ans


        