class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = float('-inf')
        
        n = len(prices)

        for i in range(n):

            for j in range(i+1,n):

                profit = prices[j] - prices[i]

                ans = max(ans,profit)
        
        return 0 if ans < 0 else ans
        


        
        