class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adjMap = defaultdict(list)

        for preReq in prerequisites:
            adjMap[preReq[0]].append(preReq[1])
    
        def bfs(start, end):
            visited = set()
            q = deque()
            q.append(start)
            
            while q:
                subject = q.popleft()
                if subject == end:
                    return True
                visited.add(subject)

                if subject in adjMap:
                    for i in adjMap[subject]:
                        if i in visited:
                            continue
                        else:
                            q.append(i)
        
            return False
        final = []
        for query in queries:
            res = bfs(query[0],query[1])
            final.append(res)
        return final
