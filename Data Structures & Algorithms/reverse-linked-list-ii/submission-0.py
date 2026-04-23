# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: 
            return head
        dummy = ListNode(0, head)
        leftNode, rightNode = dummy, head
        for _ in range(left-1):
            leftNode = leftNode.next #this will be before
            rightNode = rightNode.next #this will be on the node
        prev = None
        for _ in range(right - left + 1):
            temp = rightNode.next
            rightNode.next = prev
            prev = rightNode
            rightNode = temp
        
        leftNode.next.next = rightNode
        leftNode.next = prev
        
        return dummy.next