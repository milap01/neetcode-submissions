class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr = 0

        mx = nums[0]

        for num in nums:

            if curr < 0:

                curr = 0

            curr += num
            
            mx = max(mx,curr)
        
        return mx
            

        
        