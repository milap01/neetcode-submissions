# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p,q):

            if p and q:

                if p.val != q.val:

                    return False
                
                ans1 = dfs(p.left,q.left)
                ans2 = dfs(p.right,q.right)

                return ans1 and ans2
            elif p and not q:

                return False
            elif not p and q:

                return False
            else:

                return True
        
        return dfs(p,q)
        

        