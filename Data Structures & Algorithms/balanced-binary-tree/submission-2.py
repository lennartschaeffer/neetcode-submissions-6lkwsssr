# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0

            return 1 + max(dfs(root.left),dfs(root.right))

        if not root:
            return True

        leftHeight, rightHeight = dfs(root.left), dfs(root.right)
        print(leftHeight,rightHeight)
        if abs(leftHeight-rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


        