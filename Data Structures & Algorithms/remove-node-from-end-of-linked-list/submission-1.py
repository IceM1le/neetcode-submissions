# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur            
            cur = nxt        
        k = 1
        cur = prev if k != n else prev.next
        prev = None        
        while cur:                                    
            if k + 1 == n: nxt = cur.next.next
            else: nxt = cur.next
            cur.next = prev
            prev = cur            
            cur = nxt
            k += 1
        return prev