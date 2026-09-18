class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        dp = [-1]*(n+1)

        def rec(i):

            # pruning
            if i > n:

                return 1e9

            # base case
            if i == n:

                return 0

            # cache check
            if dp[i] != -1:

                return dp[i]

            # compute 

            ans = min(cost[i] + rec(i+1), cost[i] + rec(i+2))

            # save and return

            dp[i] = ans

            return ans
        
        ans1 = rec(0)
        ans2 = rec(1)

        ans = min(ans1,ans2)

        return ans


        