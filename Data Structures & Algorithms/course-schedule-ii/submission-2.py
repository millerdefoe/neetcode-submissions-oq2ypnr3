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

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            visiting.add(course)
            for preReq in adjMap[course]:
                if not dfs(preReq):
                    return False
            visiting.remove(course)

            visited.add(course)
            output.append(course)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        return output
