class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        dp = {}

        def rec(i):
            if i == 0:
                return nums[0], nums[0]

            if i in dp:
                return dp[i]

            prev_max, prev_min = rec(i - 1)

            curr_max = max(
                nums[i],
                nums[i] * prev_max,
                nums[i] * prev_min
            )

            curr_min = min(
                nums[i],
                nums[i] * prev_max,
                nums[i] * prev_min
            )

            dp[i] = (curr_max, curr_min)

            return dp[i]

        ans = float('-inf')

        for i in range(len(nums)):
            ans = max(ans, rec(i)[0])

        return ans









        


        