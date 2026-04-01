# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root:
            res.append([root.val])
        else:
            return []
        q = collections.deque()
        q.append(root)

        # [[2,3]]
        while len(q) > 0:
            vals = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    vals.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    vals.append(curr.right.val)
                    q.append(curr.right)
            res.append(vals) if len(vals) > 0 else None
        
        return res
            

            

