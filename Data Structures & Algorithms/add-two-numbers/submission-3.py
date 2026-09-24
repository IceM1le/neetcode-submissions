# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = 0
        dummy = ListNode()
        res = dummy 
        while l1 or l2 or tmp > 0:
            if l1:
                a = l1.val
            else:
                a = 0
            if l2:
                b = l2.val
            else:
                b = 0
            if a + b + tmp > 9:
                res.next = ListNode(a+b+tmp-10)
                tmp = 1
            else:
                res.next = ListNode(a+b+tmp)
                tmp = 0
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
