# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        curr_1 = list1
        curr_2 = list2

        head = None

        if curr_1.val <= curr_2.val:
            head = curr_1
            curr_1 = curr_1.next
        else:
            head = curr_2
            curr_2 = curr_2.next
        curr = head 

        while curr_1 or curr_2:
            if curr_1 is None or (curr_2 is not None and curr_1.val > curr_2.val):
                next_node=curr_2
                curr_2 = curr_2.next
            else:
                next_node = curr_1
                curr_1 = curr_1.next

            curr.next = next_node
            curr = next_node
        return head
                

            