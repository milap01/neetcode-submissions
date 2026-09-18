class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        state = []

        ans = []

        def rec(level):

            if level == n:

                # ans.append(state)

                # print(state)

                ans.append(state[:])

                return
            

            rec(level + 1)

            state.append(nums[level])

            rec(level + 1)

            state.pop()
        
        rec(0)

        return ans
        
            

                


        