class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0

        while n:

            rem = n % 2

            cnt += 1 if rem == 1 else 0

            n = n // 2
        
        return cnt

        