class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        for i in range(len(nums) - 2):

            for j in range(i+1,len(nums) - 1):

                for z in range(j+1,len(nums)):

                    arr = [0,0,0]

                    if nums[i] + nums[j] + nums[z] == 0:

                        arr[0] = nums[i]
                        arr[1] = nums[j]
                        arr[2] = nums[z]
                        
                        arr.sort()
                        
                        if arr not in result:

                                result.append(arr)
        
        return result


