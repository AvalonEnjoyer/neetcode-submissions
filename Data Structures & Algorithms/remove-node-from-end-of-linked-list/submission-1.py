# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return 

        second = ListNode(val=0, next=head)
        first = head

        for _ in range(n):
            first = first.next
        
        if first:
            while first.next:
                second = second.next
                first = first.next

            second, first = second.next, first.next

        if second.next == head:
            head = head.next
        else:
            second.next = second.next.next 

        return head