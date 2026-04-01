# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            # 1. Find kth node
            kth = prevGroup
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            # 2. Reverse group
            prev, curr = groupNext, prevGroup.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 3. Reconnect
            tmp = prevGroup.next   # old head → now tail
            prevGroup.next = kth
            prevGroup = tmp

            


            
        



