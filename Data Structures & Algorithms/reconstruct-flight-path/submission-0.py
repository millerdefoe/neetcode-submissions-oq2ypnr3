class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjMap = collections.defaultdict(list)
        tickets.sort()
        for start, dest in tickets:
            adjMap[start].append(dest)

        res = ["JFK"]
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if node not in adjMap:
                return False
            
            temp = list(adjMap[node])
            for i, v in enumerate(adjMap[node]):
                adjMap[node].pop(i)
                res.append(v)
                if dfs(v): return True
                adjMap[node].insert(i, v)
                res.pop()
        
            return False

        dfs("JFK")
        return res