# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # new list node, and a dummy to keep reference to the start
        newList = ListNode()
        dummy = newList
        #remember to return dummy.next
        # null, 1, 1
        # 2,4
        # 3,5
        while list1 and list2:
            #combining the two lists
            if list1.val < list2.val:
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next
                
            newList = newList.next

        if not list1 and list2:
            newList.next = list2
        elif not list2 and list1:
            newList.next = list1

        return dummy.next
        
        
            
