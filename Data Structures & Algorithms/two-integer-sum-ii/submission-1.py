class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        arr = [0,0]

        left = 0

        right = len(numbers) - 1

        while left < right:

            currSum = numbers[left] + numbers[right]

            if currSum > target:

                right = right - 1
            
            if currSum < target:

                left  = left + 1
            
            if currSum == target:

                arr[0] = left + 1
                arr[1] = right + 1

                return arr
        