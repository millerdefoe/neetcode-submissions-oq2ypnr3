# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        min_heap = []
        count = 0
        for list_ in lists:
            min_heap.append((list_.val, count, list_))
            count += 1
        heapq.heapify(min_heap)

        res_list = ListNode()
        temp = res_list

        while min_heap:
            value, _, node = heapq.heappop(min_heap)
            temp.next = node
            temp = temp.next
            node = node.next
            if node is not None:
                heapq.heappush(min_heap, (node.val, count, node))
                count += 1
        
        return res_list.next






