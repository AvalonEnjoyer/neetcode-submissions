# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        if head.next:
            slow = head.next
        else:
            return False

        if slow.next:
            fast = slow.next
        else:
            return False

        while fast:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast.next and fast.next.next:
                    fast = fast.next.next
                else:
                    return False
        return False