from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #adjMap word -> words
        #if diff == 1 add that to the adjMap for word
        if endWord == beginWord:
            return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        #minimum path and path weights are equal and non zero (BFS)
        #need a queue and since we care about length, we'd want to track layers
        #stop when value poppedleft is == target and return
        #if the q gets emptied without a return we would just return 0

        queue = deque()
        visited = set([beginWord])
        
        queue.append(beginWord)

        dist = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return dist
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            queue.append(neiWord)
            dist += 1

        return 0