# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:

        def same(root,subroot):

            if not root and not subroot:

                return True
            
            if not root or not subroot:

                return False
            
            if root.val != subroot.val:

                return False
            
            return same(root.left,subroot.left) and same(root.right,subroot.right)

        def rec(root,subroot):


            if not root:

                return False
            
            if same(root,subroot):

                return True
            
            return rec(root.left,subroot) or rec(root.right,subroot)

        return rec(root,subroot)

    

        


                    
        