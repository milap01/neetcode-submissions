from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        tail = 0

        head = -1

        ds = defaultdict(int)

        ans = 0

        def check(head):

           
            ds2 = ds.copy()
            ds2[s[head]] += 1

            max_freq = max(ds2.values())
            window_len = sum(ds2.values())

            return window_len - max_freq <= k

            

        while tail < n:

            while (head + 1) < n and check(head + 1):

                head += 1

                ds[s[head]] += 1

            ans = max(ans,head - tail + 1)

            if tail <= head:

                ele = s[tail]

                ds[ele] -= 1

                if ds[ele] == 0:

                    del ds[ele]
                
                tail += 1
            else:

                tail += 1

                head = tail - 1

        return ans


        