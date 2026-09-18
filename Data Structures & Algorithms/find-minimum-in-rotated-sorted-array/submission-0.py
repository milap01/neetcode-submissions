class Solution:
    def findMin(self, nums: List[int]) -> int:

        lo = 0

        n = len(nums)

        hi = n - 1

        while lo <= hi:

            mid = (lo + hi) // 2

            lidx = (mid + n - 1) % n

            ridx = (mid + 1) % n

            if nums[lidx] >= nums[mid] and nums[ridx] >= nums[mid]:

                return nums[mid]
            elif nums[hi] > nums[mid]:

                hi = mid - 1
            elif nums[hi] < nums[mid]:

                lo = mid + 1
        


        