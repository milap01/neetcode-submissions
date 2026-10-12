# from collections import defaultdict
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

#         state = []

#         ans = []

#         n = len(candidates)

#         def rec(level,curr):

#             if curr == target:

#                 tmp = state[:]

#                 tmp.sort()

#                 ans.append(tmp)

#                 return 

#             if level >= n or curr > target:

#                 return 
   
#             # two choices

#             rec(level+1,curr)
            
#             state.append(candidates[level])

#             rec(level+1,curr + candidates[level])

#             state.pop()
        
#         rec(0,0)

#         ans.sort()

#         if ans:

#             final = [ans[0]]

#             curr = ans[0]

#             for idx in range(1,len(ans)):

#                 if curr != ans[idx]:

#                     curr = ans[idx]
#                     final.append(curr)

#             return final
#         else:

#             return []


from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        n = len(candidates)
        state = []

        def rec(level, curr):
            if curr == target:
                ans.append(state[:])
                return

            if level >= n or curr > target:
                return

            for i in range(level, n):
                # Skip duplicates at the same recursion level
                if i > level and candidates[i] == candidates[i - 1]:
                    continue

                # Since candidates are sorted, no need to continue
                if curr + candidates[i] > target:
                    break

                state.append(candidates[i])
                rec(i + 1, curr + candidates[i])
                state.pop()

        rec(0, 0)
        return ans

            

        