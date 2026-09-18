class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1]*(n+1)

        def rec(i):


            # pruning
            if i > n:

                return 0

            # base case
            if i == n:

                return 1

            # cache check
            if dp[i] != -1:

                return dp[i]

            # compute

            ways = rec(i+1) + rec(i+2)

            # save and return

            dp[i] = ways

            return ways
        
        return rec(0)

        