class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = 0

        right = len(nums) - 1

        pivot = 0

        while left <= right:

            mid = (left + right) // 2

            if ( mid == len(nums) - 1 and left == right) or ( mid == 0 and left == right) :

                pivot = left

                break
            
            if (nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]) or (nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]) :

                pivot =   mid

                break

            if nums[mid] > nums[right]:

                left = mid + 1

            if nums[mid] < nums[right]:

                right = mid - 1
            
            

        print(pivot)
            
        
        left1 = 0
        right1 = pivot - 1

        if len(nums) == 2:

            if nums[0] == target:
                return 0
            
            elif nums[1] == target:

                return 1
            else:

                return -1
        
        

        while left1 <= right1:

            mid = (left1 + right1) // 2

            if nums[mid] == target:

                return mid
            
            if nums[mid] > target:

                right1 = mid - 1
            
            if nums[mid] < target:

                left1 = mid + 1

        left2 = pivot
        right2 = len(nums) - 1

        while left2 <= right2:

            mid = (left2 + right2) // 2

            if nums[mid] == target:

                return mid
            
            if nums[mid] > target:

                right2 = mid - 1
            
            if nums[mid] < target:

                left2 = mid + 1
        
        if pivot == 0:

            if len(nums) == 1:

                if nums[0] == target:
                    return  0
                else:
                    return -1
            
            if len(nums) > 1:

                if nums[0] == target:
                    return 0
                if nums[1] == target:

                    return 1
                else:

                    return -1
        
        return -1





                


        