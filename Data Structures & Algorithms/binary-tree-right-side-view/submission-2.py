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

        while len(q):
            rightMost = None
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    rightMost = curr
                        
            if rightMost:
                rightSide.append(rightMost.val)
        
        return rightSide
                



        