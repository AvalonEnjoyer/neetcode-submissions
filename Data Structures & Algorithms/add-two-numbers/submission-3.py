# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if not l1:
        #     return l2
        # elif not l2:
        #     return l1

        head = ListNode(0)
        cur = head
        cur1, cur2 = l1, l2
        carry = 0 

        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0

            sum = val1 + val2 + carry
            carry = 0
            
            if sum > 9:
                carry = 1
                sum = sum%10
            
            cur.val = sum
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            
            if carry > 0 or cur1 or cur2:
                temp = ListNode(carry)
            else:
                temp = None
            cur.next = temp
            cur = temp

        return head

            