class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for i in range(len(routes)):
            for j in routes[i]:
                stop_to_routes[j].add(i) #mapping a stop to a route
        
        visited_routes = set()
        visited_stops = set([source])

        q = deque()
        for i in stop_to_routes[source]:
            q.append((i, 1))
            visited_routes.add(i)

        while q:
            route, buses = q.popleft()
            if target in routes[route]:
                return buses
            
            for stop in routes[route]:
                if stop not in visited_stops:
                    for i in stop_to_routes[stop]:
                        if i not in visited_routes:
                            q.append((i, buses + 1))
                            visited_stops.add(stop)
                            visited_routes.add(i)
        return -1

