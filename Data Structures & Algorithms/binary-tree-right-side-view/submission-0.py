# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
            queue=collections.deque()
            ans=[]
            if not root:
                return ans
            queue.append(root)
            while queue:
                leng=len(queue)
                level=[]
                for i in range(leng):
                    node=queue.popleft()
                    if node:
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if level:
                    ans.append(level)
            return ans
        level=levelOrder(root)
        ans=[]
        for i in level:
            ans.append(i[-1])
        return ans
