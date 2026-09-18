# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        arr = []

        def run(root,arr):

            if not root:

                return
            
            run(root.left,arr)
            arr.append(root.val)
            run(root.right,arr)
        
        run(root,arr)

        return arr

        