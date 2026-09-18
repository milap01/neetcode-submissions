class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:

            return nums[0]

        dp = [-1]*(n+1)
        dp2 = [-1]*(n+1)

        def rec(i):

            # pruning

            # base case
  
            if i >= n:

                return 0

            # cache check
            if dp[i] != -1:

                return dp[i]

            # compute

            ans1 = rec(i+1)
            ans2 = rec(i+2) + nums[i]

            ans = max(ans1,ans2)

            # save and return

            dp[i] = ans

            return ans
        def rec2(i):

            # pruning

            # base case
  
            if i >= n-1:

                return 0

            # cache check
            if dp2[i] != -1:

                return dp2[i]

            # compute

            ans1 = rec2(i+1)
            ans2 = rec2(i+2) + nums[i]

            ans = max(ans1,ans2)

            # save and return

            dp2[i] = ans

            return ans

        ans1 = rec(1)
        ans2 = rec2(0)

        return max(ans1,ans2)



        
        





        