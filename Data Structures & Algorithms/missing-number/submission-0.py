class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        xor = 0

        for num in range(len(nums) + 1):

            xor = xor ^ num
        
        xor2 = 0

        for num in nums:

            xor2 = xor2 ^ num
    

        return xor2 ^ xor
        