# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            ans=max(ans,dfs(node.left)+dfs(node.right))
            return max(dfs(node.left)+1,dfs(node.right)+1)
        dfs(root)
        return ans

            
        
            