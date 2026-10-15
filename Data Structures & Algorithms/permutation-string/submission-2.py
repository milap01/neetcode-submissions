from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        tail = 0

        head = -1

        n = len(s2)

        ds = defaultdict(int)

        k = len(s1)

        ds_ = defaultdict(int)

        for char in s1:

            ds_[char] += 1
        
        j = 0

        for i in range(n):

            ele = s2[i]

            ds[ele] += 1

            if (i - j + 1) == k:

                if ds == ds_:

                    return True
                else:

                    curr = s2[j]

                    ds[curr] -= 1

                    if ds[curr] == 0:

                        del ds[curr]
                    
                    j += 1
        
        return False
            


            




            
        