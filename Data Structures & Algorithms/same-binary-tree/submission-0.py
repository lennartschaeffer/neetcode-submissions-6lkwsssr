# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case is gonna be if not p and not q
        #compare p and q left right subtrees, if they dont match
        #return false, otherwise call method recursively on 
        #left and right nodes
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        print(p.val,q.val)
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)