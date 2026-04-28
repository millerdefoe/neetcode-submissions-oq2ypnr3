class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = defaultdict(list)
        eqn_to_val = {}
        for eqn, val in zip(equations,values):
            eqn_to_val[tuple(eqn)] = val
            eqn_to_val[tuple(eqn[::-1])] = 1 / val

        for equation in equations:
            adjMap[equation[0]].append(equation[1])
            adjMap[equation[1]].append(equation[0])
        res = []
        for query in queries:
            # bfs to find path 
            if query[1] not in adjMap or query[0] not in adjMap:
                res.append(-1)
            elif query[0] in adjMap and query[1] in adjMap[query[0]]:
                res.append(eqn_to_val[tuple((query[0],query[1]))])
            elif query[0] == query[1]:
                res.append(1)
            else:
                #bfs to find the route
                q = deque()
                q.append((query[0],1))
                found = 0
                visited = set()
                while q:
                    letter, product = q.popleft()

                    if letter == query[1]:
                        res.append(product)
                        found = 1
                        break
                    
                    for nei in adjMap[letter]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append((nei, product * eqn_to_val[tuple((letter,nei))]))
                if not found:
                    res.append(-1)
        
        return res
            