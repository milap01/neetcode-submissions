# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        dq = deque()

        dq.append(root)

        ans = []

        while dq:

            n = len(dq)

            tmp = []

            for _ in range(n):

                node = dq.popleft()

                if node:
                    tmp.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
            
            if tmp:
                ans.append(tmp)
        
        return ans







