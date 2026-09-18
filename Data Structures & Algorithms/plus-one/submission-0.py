class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = int("".join(map(str,digits)))

        new = num + 1

        dq = deque()
        while new:

            rem = new % 10

            dq.appendleft(rem)

            new = new // 10

        return list(dq)        