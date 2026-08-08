# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        list_recorded = []
        cur = head
        while not cur is None:
            list_recorded.append(cur)
            cur = cur.next
        n = len(list_recorded)
        right = list_recorded[-1]
        for i in range((n + 1) // 2):
            left = list_recorded[i]
            right = list_recorded[n - i - 1]
            left.next = right
            right.next = list_recorded[i + 1]
        right.next = None
            
