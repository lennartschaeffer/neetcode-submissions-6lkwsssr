class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            #if we are at the current index, return the value
            if i == index:
                return curr.val
            #otherwise, move to next node and increment index
            curr = curr.next
            i += 1
        #if we are here, it means we're out of bounds, so we return -1
        return -1
            

    def insertHead(self, val: int) -> None:
        #create new head node and assign it the value
        new_head = ListNode(val)
        new_head.next = self.head.next
        self.head.next = new_head
        #if the list is empty, set the tail to this new head as well
        if new_head.next is None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        #whatever the current tail is, set its next pointer to the new tail
        self.tail.next = new_tail
        #now set the tail pointer to this new tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        #check if the current node exists, and if it has a next node
        #set pointer of the node before the node to remove to the next one 
        #after that
        while curr and i < index:
            i += 1
            curr = curr.next
            
        if curr and curr.next:
            #if the node we want to remove is the tail, we can just
            #set the tail pointer to the current node so nothig is pointing
            #to it anymore
            if curr.next == self.tail:
                self.tail = curr
            #if its not the tail, point the node's next pointer to the 
            #next next one
            curr.next = curr.next.next
            return True

        return False

        

    def getValues(self) -> List[int]:
        curr = self.head.next
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        return nodes
