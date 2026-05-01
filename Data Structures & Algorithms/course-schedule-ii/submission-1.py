class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        for course, preReq in prerequisites:
            adjMap[course].append(preReq)
        
        # we've built the adjMap

        visited = set()

        # will track all visited to prevent repeat work (a node is visited when all its neighbours are)

        visiting = set()
        # to find cycles
        output = []
        cycle = False
        def dfs(course):
            if course in visiting:
                nonlocal cycle
                cycle = True
                return
            
            if course in visited:
                return
            visiting.add(course)
            for preReq in adjMap[course]:
                dfs(preReq)
            visiting.remove(course)

            visited.add(course)
            output.append(course)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)

        if cycle:
            return []
        else:
            return output