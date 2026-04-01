# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # iterate through the list, get the count, and then iterate again and just
        #remove count - nth node
        if not head.next:
            head = None
            return head

        count = 0
        curr = head
        while curr:
            count +=1 
            curr = curr.next

        dummy = head
        
        n = count - n - 1
        if n < 0:
            print(head.val, head.next.val)
            head = head.next
            return head

        for i in range(n): #[1,2] count = 2 target = 2
            print(head.val)
            head = head.next

        if head.next:
            print(head.val,head.next.val)
            head.next = head.next.next

        return dummy