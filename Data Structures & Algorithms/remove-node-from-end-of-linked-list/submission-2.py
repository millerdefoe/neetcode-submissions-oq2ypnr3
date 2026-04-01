# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leader = head
        follower = dummy = ListNode(0, head)




        for i in range(n):
            leader = leader.next

        while leader:
            follower = follower.next
            leader = leader.next
        
        follower.next = follower.next.next

        return dummy.next