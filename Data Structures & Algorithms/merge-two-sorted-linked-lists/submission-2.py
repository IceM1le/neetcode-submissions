# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        head = None
        while list1 or list2:
            if not list1:
                list3 = list2
                list2 = list2.next
            elif not list2:
                list3 = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                list3 = list1
                list1 = list1.next
            else:
                list3 = list2
                list2 = list2.next
            if head is None:
                cur = list3
                head = cur
            else:
                cur.next = list3
                cur = list3

        return head