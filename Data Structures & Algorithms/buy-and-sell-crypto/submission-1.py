class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mx = prices[-1]

        n = len(prices)

        ans = float('-inf')

        for i in range(n-2,-1,-1):

            profit = mx - prices[i]

            ans = max(ans,profit)

            mx = max(mx,prices[i])
        
        return ans if ans >= 0 else 0


        


        
        