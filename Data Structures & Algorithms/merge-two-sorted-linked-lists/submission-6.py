# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = False
        head = None 
        curr_1 = list1
        curr_2 = list2

        while curr_1 or curr_2:
            if curr_1 is None or (curr_2 is not None and curr_1.val > curr_2.val):
                next_node=curr_2
                curr_2 = curr_2.next
            else:
                next_node = curr_1
                curr_1 = curr_1.next
            # else:
            #     next_node = curr_2
            #     curr_2 = curr_2.next

            if not prev:
                head = ListNode(val=next_node.val,next=None)
                prev = head
            else:
                curr = ListNode(val=next_node.val, next=None)
                prev.next = curr
                prev = curr
        return head
                

            