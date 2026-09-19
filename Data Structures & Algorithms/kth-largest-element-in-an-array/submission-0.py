class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort(reverse=True)

        K = 0

        prev = 10001

        for num in nums:

            if prev != num:

                K += 1

                if K == k:

                    return num
            
        

        




        