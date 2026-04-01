# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get the middle of the linked list using f & s ptr

        slow,fast = head,head
        l1 = slow

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None
        #reverse l2
        prev = None
        while l2:
            nextNode = l2.next
            l2.next = prev
            prev = l2
            l2 = nextNode
        first,second = head,prev
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1,tmp2
        #combine the two lists into one
        
            


