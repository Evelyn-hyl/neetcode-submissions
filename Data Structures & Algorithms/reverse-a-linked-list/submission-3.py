# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        ptr_1 = 0
        ptr_2 = 0

        if head.next != None:
            ptr_1 = head.next

            if ptr_1.next != None:
                ptr_2 = ptr_1.next
        
        
        head.next = None
        
        while ptr_2 != 0 and ptr_2.next != None:
            ptr_1.next = head
            head = ptr_1
            ptr_1 = ptr_2
            ptr_2 = ptr_1.next
        
        if ptr_1 != 0:
            ptr_1.next = head
            head = ptr_1
        
        if ptr_2 != 0:
            ptr_2.next = head
            head = ptr_2

        return head
        
            


