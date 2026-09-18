class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for string in strs:

            count = [0]*26

            for char in string:

                count[ord(char) - ord('a')] += 1
            
            mp[tuple(count)].append(string)
        
        return list(mp.values())

        
        

        