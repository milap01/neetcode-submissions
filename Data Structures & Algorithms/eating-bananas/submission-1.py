class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        lo = 1

        hi = max(piles)

        ans = -1

        def check(k):

            time = 0

            for pile in piles:

                time += math.ceil(pile / k)
            
            return time <= h

        while lo <= hi:

            mid = (lo + hi) // 2

            if check(mid):

                ans = mid

                hi = mid - 1
            else:

                lo = mid + 1
        
        return ans



        