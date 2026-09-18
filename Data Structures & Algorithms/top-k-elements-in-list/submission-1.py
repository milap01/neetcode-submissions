class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = defaultdict(int)

        for num in nums:

            mp[num] += 1

        sorted_mp = sorted(mp.items(),key=lambda item : item[1],reverse = True)

        # print(sorted_mp)

        ans = []

        for i in range(k):

            ans.append(sorted_mp[i][0])
        
        return ans
        