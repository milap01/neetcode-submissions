class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[-1]*(amount+1) for _ in range(n)]

        def rec(i,curr):

            # pruning
            if curr > amount or i >= n:
                return float('inf')

            # base case
            if curr == amount:

                return 0

            # cache check
            if dp[i][curr] != - 1:

                return dp[i][curr]

            # compute
            ans = float('inf')

            ans = min(rec(i+1,curr),rec(i,curr+coins[i]) + 1)

            # save and return
            dp[i][curr] = ans
            return ans
        
        return rec(0,0) if rec(0,0) != float('inf') else -1
        