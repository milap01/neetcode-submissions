from collections import deque,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n = len(s)

        tail = 0

        head = -1

        ans = []

        ds = defaultdict(int)

        missing = len(t)

        best_start = 0

        best_len = float('inf')

        for char in t:

            ds[char] += 1
        
        while tail < n:

            while (head + 1) < n and missing > 0:

                head += 1

                ele = s[head]

                if ds[ele] > 0:

                    missing -= 1
                ds[ele] -= 1
            
            if missing == 0:

                if best_len > (head - tail + 1):

                    best_len = head - tail + 1
                    best_start = tail
            
            if tail <= head:

                ele = s[tail]
                ds[ele] += 1

                if ds[ele] > 0:

                    missing += 1
                
                tail += 1
            else:

                tail += 1
                head = tail - 1

        if best_len == float('inf'):

            return ""
        else:

            return s[best_start:best_start+best_len]        



                



        

        



        