# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None


        def mergeSorted(listA, listB)->Optional[ListNode]:
            
            head = ListNode()
            cur = head
            while listA and listB:
                if listA.val < listB.val:
                    cur.next = listA
                    listA = listA.next
                    cur = cur.next
                else:
                    cur.next = listB
                    listB = listB.next
                    cur = cur.next
            if listA:
                cur.next = listA
            elif listB:
                cur.next = listB
            
            return head.next

        for i in range(1, len(lists)):
            lists[i] = mergeSorted(lists[i-1], lists[i])
        
        return lists[-1]
            
            