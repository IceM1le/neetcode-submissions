# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        set_elem = set()
        while cur:            
            if cur in set_elem:
                return True
            set_elem.add(cur)
            cur = cur.next
        return False