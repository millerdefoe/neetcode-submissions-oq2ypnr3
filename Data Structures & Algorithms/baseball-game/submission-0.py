class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreList = collections.deque()
        for i in operations:
            if i == 'C':
                scoreList.pop()
            elif i == 'D':
                scoreList.append(scoreList[-1] * 2)
            elif i == '+':
                scoreList.append(scoreList[-1] + scoreList[-2])
            else:
                scoreList.append(int(i))
        
        return sum(scoreList)