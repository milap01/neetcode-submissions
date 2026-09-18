# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        

        def dfs(root,mx):

            if root:
                ans = 0
                if mx <= root.val:

                    ans = 1

                mx = max(mx,root.val)

                x = dfs(root.left,mx)
                y = dfs(root.right,mx)

                return ans + x + y
            else:

                return 0
        
        return dfs(root,root.val)

                    


        