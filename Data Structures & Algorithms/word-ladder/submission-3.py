from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #adjMap word -> words
        #if diff == 1 add that to the adjMap for word
        if endWord == beginWord:
            return 0

        def compareWords(word1: str, word2: str)-> bool:
            diff = 0
            for c1,c2 in zip(word1,word2):
                if c1 != c2:
                    diff += 1
            
            return diff == 1

        wordList.append(beginWord)

        adjMap = defaultdict(list)
        for wordKey in wordList:
            for wordCandidate in wordList:
                if compareWords(wordKey, wordCandidate):
                    adjMap[wordKey].append(wordCandidate)

        print(adjMap)

        #minimum path and path weights are equal and non zero (BFS)
        #need a queue and since we care about length, we'd want to track layers
        #stop when value poppedleft is == target and return
        #if the q gets emptied without a return we would just return 0

        queue = deque()
        visited = set()
        
        queue.append(beginWord)
        dist = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return dist
                
                if word in visited:
                    continue
                
                visited.add(word)
                for nei in adjMap[word]:
                    if nei not in visited:
                        queue.append(nei)
            dist += 1

        return 0