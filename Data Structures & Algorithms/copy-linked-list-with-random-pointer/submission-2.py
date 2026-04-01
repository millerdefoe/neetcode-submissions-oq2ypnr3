"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #build the full list first

        list1 = head
        dummy = list2 =  Node(0)
        hashM = {}
        

        while list1:
            list2.next = Node(list1.val)
            list2 = list2.next
            hashM[list1] = list2
            list1 = list1.next

        list1 = head
        list2 = dummy
        while list1:
            list2 = list2.next
            
            if list1.random == None:
                list2.random = None
            else:
                list2.random = hashM[list1.random]
            list1 = list1.next

        return dummy.next








