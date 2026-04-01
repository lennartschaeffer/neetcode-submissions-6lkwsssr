# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs, and return the rightmost node in the level
        q = collections.deque()
        q.append(root)
        rightSide = []
        if root:
            rightSide.append(root.val)
        else:
            return []

        while len(q):
            vals = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    vals.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    vals.append(curr.right.val)
                        
            if len(vals):
                rightSide.append(vals[-1])
        
        return rightSide
                



        