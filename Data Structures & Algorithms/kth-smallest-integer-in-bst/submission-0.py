# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #get the size of the left sub tree, if k < size, it's 
        #in the left, otherwise it's in the right
        #while im traversing, keep track of the smallest elements
        #up to k

        self.vals = []

        def dfs(root):
            if not root:
                return

            if root.val not in self.vals:
                self.vals.append(root.val)
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        self.vals.sort()
        print(self.vals)
        return self.vals[k-1]