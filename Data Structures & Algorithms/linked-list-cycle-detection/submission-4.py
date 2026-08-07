# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        cur2 = head
        while cur2 and cur2.next:  
            cur = cur.next
            cur2 = cur2.next.next
            if cur == cur2:
                return True          
        return False