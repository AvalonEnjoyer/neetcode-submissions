# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
            if not head:
                return None
            
            newHead = head
            if head.next:
                newHead = self.reverseList(head.next)
                head.next.next = head
            head.next = None

            return newHead

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        prev = start 

        for _ in range(left-1):
            prev = prev.next
        
        sublist_head = prev.next
        print(sublist_head.val)
        sublist_tail = sublist_head

        for _ in range(right-left):
            sublist_tail = sublist_tail.next
        print(sublist_tail.val)
        
        next_node = sublist_tail.next
        sublist_tail.next = None
        reversed_sublist = self.reverseList(sublist_head)
        prev.next = sublist_tail
        # print(reversed_sublist.val)
        sublist_head.next = next_node
        
        return start.next
        
        