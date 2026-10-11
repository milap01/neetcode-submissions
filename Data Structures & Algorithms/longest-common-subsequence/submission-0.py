class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        dp = [[-1]*(m) for _ in range(n)]

        def rec(i,j):

            if i >= n or j >= m:

                return 0
            
            if dp[i][j] != -1:

                return dp[i][j]

            count = 0
            if text1[i] == text2[j]:

                count = 1 + rec(i+1,j+1)
            else:
                count = max(rec(i,j+1),rec(i+1,j)) 
            
            dp[i][j] = count

            return count
        
        ans = 0

        for i in range(n):

            for j in range(m):

                ans = max(ans,rec(i,j))
        
        return ans


 




        