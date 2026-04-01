# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return
            if validPath(root, node, root.val):
                self.count += 1

            dfs(node.left)
            dfs(node.right)

        def validPath(current, target, maxSoFar):
            if not current:
                return False
            
            if maxSoFar > target.val:
                return False
            
            if current == target:
                return True

            maxSoFar = max(maxSoFar, current.val)

            return validPath(current.left, target, maxSoFar) or validPath(current.right, target, maxSoFar)

        dfs(root)

        return self.count

