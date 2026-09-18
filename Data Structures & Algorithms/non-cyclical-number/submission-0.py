class Solution:
    def isHappy(self, n: int) -> bool:

        def compute(n):

            ans = 0

            while n:

                rem = n % 10

                ans += (rem)** 2

                n = n // 10
            
            return ans
        
        st = set()

        while n != 1:

            st.add(n)

            n = compute(n)

            if n in st:

                return False
        
        return True

            




        