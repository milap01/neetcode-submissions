class Solution:
    def myPow(self, x: float, n: int) -> float:

        def binpow(a,b):

            if b == 0:

                return 1
            elif b % 2:

                return a * binpow(a,b-1)
            elif b % 2 == 0:

                tmp = binpow(a,b//2)

                return tmp * tmp
        
        if n < 0:

            ans = binpow(x,-n)

            return (1 / ans)
        else:

            ans = binpow(x,n)

            return ans

        