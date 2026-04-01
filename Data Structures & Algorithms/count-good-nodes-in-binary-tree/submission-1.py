# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, currentMax):
            if not node:
                return 0
            
            res = 1 if node.val >= currentMax else 0
            currentMax = max(currentMax, node.val)
            res += dfs(node.left, currentMax)
            res += dfs(node.right, currentMax)

            return res

        return dfs(root,root.val)

            
            
            
            

