# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #create a helper method that checks the constraints
        def isValidRightSubtree(currentVal, node):
            if not node:
                return True
            
            if node.val <= currentVal:
                return False
            
            return isValidRightSubtree(currentVal,node.left) and isValidRightSubtree(currentVal, node.right)

        def isValidLeftSubtree(currentVal,node):
            if not node:
                return True
            
            if node.val >= currentVal:
                return False
            
            return isValidLeftSubtree(currentVal,node.left) and isValidLeftSubtree(currentVal, node.right)

        if not root:
            return True

        if not isValidRightSubtree(root.val,root.right) or not isValidLeftSubtree(root.val, root.left):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

        

        
            