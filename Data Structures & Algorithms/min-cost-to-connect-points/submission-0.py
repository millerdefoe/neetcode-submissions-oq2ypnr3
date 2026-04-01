class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #djikstras can be used as its a min cost path in a positive weighted graph
        #we make use of a minHeap to choose which path to explore next. This value of the path is the sum of all weights take before it
        # its a bfs type algo making use of a priority q / minheap
        # an approach i can take is to make a adjList with tuples of coordinate, manhattan dist. Then perform djikstras on that
        #lets make the adjList first

        adjList = {(i,j):[] for i,j in points}

        for s1,s2 in points:
            for t1,t2 in points:
                dist = abs(s1-t1) + abs(s2-t2)
                if dist != 0:
                    adjList[(s1,s2)].append((dist,(t1,t2))) # (DISTANCE, (TARGET X, TARGET Y))
        
        minHeap = []
        visited = set()
        tripCost = 0
        #start from a random point 
        # Initialize heap with starting node
        heapq.heappush(minHeap, (0, tuple(points[0])))
        
        while minHeap and len(visited) < len(points):
            dist, target = heapq.heappop(minHeap)
            if target in visited:
                continue

            visited.add(target)
            tripCost += dist

            for nei in adjList[target]:
                if nei[1] not in visited:
                    heapq.heappush(minHeap, nei)
        
        return tripCost