# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = head, head
        group_prev = dummy
        while fast:
            count_node = fast
            for _ in range(k):
                if not count_node:
                    return dummy.next
                count_node = count_node.next
            cur = slow
            prev = None
            for i in range(k):                    
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt                      
            group_prev.next = prev            
            slow.next = cur
            group_prev = slow
            fast = fast.next
            slow = fast
        return dummy.next