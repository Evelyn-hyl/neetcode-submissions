# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = set()
        while head:
            if head in seen_nodes:
                return True
            else:
                temp = head.next
                seen_nodes.add(head)
                head = temp
        
        return False

