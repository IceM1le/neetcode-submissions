# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = 0
        cur1, cur2 = l1, l2
        while cur1:
            sum_val = cur1.val + cur2.val + tmp
            if sum_val > 9:
                tmp = 1
                cur1.val = sum_val - 10
            else:
                tmp = 0
                cur1.val = sum_val
            if cur1.next or cur2.next:
                if not cur1.next:
                    cur1.next = ListNode(0)
                if not cur2.next:
                    cur2.next = ListNode(0)                
            else:
                if tmp: 
                    cur1.next = ListNode(1)
                    cur1 = cur1.next
            cur1, cur2 = cur1.next, cur2.next

        return l1    