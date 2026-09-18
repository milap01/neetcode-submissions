class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        tail = 0

        head = -1

        ds = set()

        ans = 0

        n = len(s)

        def check(x):

            if s[x] not in ds:

                return True
            else:

                return False

        while tail < n:

            while (head + 1) < n and check(head+1):

                head = head + 1

                ds.add(s[head])
            
            ans = max(ans,head - tail + 1)

            if tail <= head:

                ele = s[tail]

                ds.discard(ele)

                tail += 1
            else:

                tail = tail + 1

                head = tail - 1
        
        return ans

            


                
        