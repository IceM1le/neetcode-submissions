# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return 
        import heapq
        heap = []
        for i, lst in enumerate(lists): heapq.heappush(heap, (lst.val, i, lst))
        dummy = ListNode()
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next: heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next