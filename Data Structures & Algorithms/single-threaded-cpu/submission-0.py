class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_list = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        task_list.sort()
        
        cur_time = 0
        task_idx = 0
        result = []
        min_heap = []
        while len(result) < len(task_list):
            while task_idx < len(task_list) and task_list[task_idx][0] <= cur_time:
                heapq.heappush(min_heap, (task_list[task_idx][1], task_list[task_idx][2]))
                task_idx += 1
            
            if not min_heap:
                cur_time = task_list[task_idx][0]
            else:
                processing_time, task_no = heapq.heappop(min_heap)
                cur_time += processing_time
                result.append(task_no)

        return result
        