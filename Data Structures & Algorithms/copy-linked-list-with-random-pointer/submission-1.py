"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {}
        curr = head

        while curr:
            newNode = Node(curr.val)
            oldToNew[curr] = newNode
            curr = curr.next

        curr = head

        while curr:
            nodeToUpdate = oldToNew[curr]
            nodeToUpdate.next = oldToNew.get(curr.next, None)
            nodeToUpdate.random = oldToNew.get(curr.random, None)
            curr = curr.next

        return oldToNew.get(head,None)