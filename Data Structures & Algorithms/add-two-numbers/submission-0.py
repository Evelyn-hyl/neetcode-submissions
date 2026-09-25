# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        
        def sum_lists(last_quo: int, l1: Optional[ListNode], l2: Optional[ListNode], ptr: ListNode):
            if not l1 and not l2:
                if last_quo > 0:
                    ptr.next = ListNode(last_quo)
                return
            
            l1_val, l1_next = 0, None
            l2_val, l2_next = 0, None

            if l1:
                l1_val = l1.val
                l1_next = l1.next
            if l2:
                l2_val = l2.val
                l2_next = l2.next
            
            total = l1_val + l2_val + last_quo
            quo = total // 10
            rem = total % 10
            ptr.next = ListNode(rem)
            ptr = ptr.next

            return sum_lists(quo, l1_next, l2_next, ptr)

        sum_lists(0, l1, l2, tail)

        return dummy.next
        