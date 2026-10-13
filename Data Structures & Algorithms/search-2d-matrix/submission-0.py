class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # mlogn we can do first

        def check(arr,target):

            lo = 0
            hi = len(arr) - 1

            while lo <= hi:

                mid = (lo + hi) // 2

                if arr[mid] == target:

                    return True
                elif arr[mid] > target:

                    hi = mid - 1
                else:
                    lo = mid + 1
            
            return False

        for curr in matrix:

            if check(curr,target):

                return True
        
        return False
            



