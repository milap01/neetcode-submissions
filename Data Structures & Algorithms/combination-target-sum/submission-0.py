class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)

        ans = []

        state = []

        def rec(level,target):

            if target < 0:

                return 

            if target == 0 or level == n:

                if target == 0:
                    ans.append(state[:])
                    
                return

            rec(level + 1,target)

            state.append(nums[level])

            rec(level,target-nums[level])

            state.pop()
        
        rec(0,target)

        return ans
        

        