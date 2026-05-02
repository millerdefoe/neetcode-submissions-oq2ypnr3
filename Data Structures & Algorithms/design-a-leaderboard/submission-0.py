import heapq
from collections import defaultdict

class Leaderboard:
    def __init__(self):
        #hashmap of playerId -> score
        self.scoreMap = defaultdict(int)



    def addScore(self, playerId: int, score: int) -> None:
        self.scoreMap[playerId] -= score

    def top(self, K: int) -> int:
        #maxHeap implementation just pop k elements
        print(f"{self.scoreMap.items()=}")
        maxHeap = list(self.scoreMap.values())
        heapq.heapify(maxHeap)
        res = 0
        for _ in range(K):
            res += heapq.heappop(maxHeap)
        return -res


    def reset(self, playerId: int) -> None:
        del self.scoreMap[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
