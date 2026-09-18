class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()

        if n == 0:

            return 0

        curr = nums[0]

        length = 1

        mx = 1

        print(nums)

        for i in range(1,n):

            if nums[i] == (curr + 1):

                length += 1

                curr = nums[i]
            elif nums[i] == curr:
                continue
            else:

                length = 1 

                curr = nums[i]
            
            mx = max(mx,length)
            
        return mx




        