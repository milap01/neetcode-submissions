class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [-1]*(n+1)

        def rec(i):

            # pruning
            if i > n:

                return -1e9
            
            if i == n:

                return 0

            # base case
            if i == n-1:

                return nums[i]

            # cache check
            if dp[i] != -1:

                return dp[i]

            # compute
            ans = -1e9

            dontake = rec(i+1)

            take = nums[i] + rec(i+2)

            ans = max(dontake,take)

            # save and return

            dp[i] = ans

            return ans
        
        ans = rec(0)

        return ans
        


        

        