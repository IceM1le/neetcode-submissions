# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        cur2 = head
        while cur:  
            cur = cur.next
            cur2 = cur2.next
            if cur2 is None:
                return False
            else:
                cur2 = cur2.next
            if cur2 is None:
                return False
            if cur == cur2:
                return True          
        return False