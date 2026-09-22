class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1]*n for _ in range(m)]
        

        def rec(i,j):

            # pruning
            if i >= m or j >= n:

                return 0

            # base case

            if i == m-1 and j == n-1:

                return 1

            # cache check
            if dp[i][j] != -1:

                return dp[i][j]

            # compute

            ways = rec(i+1,j) + rec(i,j+1)

            # save and return

            dp[i][j] = ways

            return ways
        
        return rec(0,0)
