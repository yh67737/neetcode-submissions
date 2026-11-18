# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,left,right):
            if not root:
                return True
            if root.val<=left or root.val>=right:
                return False
            if root.left:
                if not valid(root.left,left,root.val):
                    return False
            if root.right:
                if not valid(root.right,root.val,right):
                    return False

            return True
        return valid(root,float("-inf"),float("inf"))
        