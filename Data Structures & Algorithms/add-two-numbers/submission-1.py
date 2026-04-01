# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        top = l1
        bottom = l2
        dummy = ListNode()
        cur = dummy
        carryover = 0
        while top or bottom or carryover:
            v1 = top.val if top else 0
            v2 = bottom.val if bottom else 0

            val = v1 + v2 + carryover

            carryover = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            top = top.next if top else None
            bottom = bottom.next if bottom else None
            


        return dummy.next
            
            
            
        