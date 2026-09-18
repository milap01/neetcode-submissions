class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in range(len(s)):

            if  s[i].isalpha() or s[i] == '0' or s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6' or s[i] == '7'or s[i] == '8' or s[i] == '9':

                arr.append(s[i])
        
        print(arr)


        left = 0

        right = len(arr) -  1

        

        while left <= right:

            if arr[left].lower() != arr[right].lower():

                return False
            left = left + 1
            right = right - 1

        return True
            
                
        