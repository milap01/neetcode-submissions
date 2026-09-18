# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = -1

        cnt = k

        def rec(root):

            nonlocal ans,cnt

            if root:

                rec(root.left)

                if cnt == 0:

                    return
                
                cnt-= 1

                if cnt == 0:

                    ans = root.val
                    return
                
                rec(root.right)
            
        
        rec(root)

        return ans



        