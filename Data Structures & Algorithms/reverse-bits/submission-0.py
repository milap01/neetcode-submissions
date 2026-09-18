class Solution:
    def reverseBits(self, n: int) -> int:

        pos = []

        while n:

            rem = n % 2

            pos.append(rem)
            
            n = n // 2
        
        pos.reverse()
        
        rem = 32 - len(pos)

        bits = [0]*rem

        pos = bits + pos

        ans = 0

        for i in range(31,-1,-1):

            if pos[i] == 1:

                ans = ans + (2 ** i) * (pos[i])

        
        return ans




        