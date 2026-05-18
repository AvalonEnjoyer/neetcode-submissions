# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = ListNode(0, head)

        left_start, cur = start, head

        for _ in range(left-1):
            left_start = left_start.next
            cur = cur.next

        prev = None
        for _ in range(right-left+1):
            tempLeft = cur.next
            cur.next = prev
            prev, cur = cur, tempLeft

        left_start.next.next = cur
        left_start.next = prev

        return start.next
