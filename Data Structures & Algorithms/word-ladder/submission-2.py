class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = list(set(wordList + [beginWord]))
        adjMap = {i:[] for i in wordList}

        for i in range(len(wordList)-1):
            word1 = wordList[i]
            for word2 in wordList[i+1:]:
                difference = 0
                for k in range(len(word1)):
                    if word1[k] != word2[k]:
                        difference += 1
                if difference == 1:
                    adjMap[word1].append(word2)
                    adjMap[word2].append(word1)

        
        q = deque()
        q.append(beginWord)
        transformations = 1
        visited = set()
        visited.add(beginWord)
        def bfs():
            nonlocal transformations
            while q:
                for _ in range(len(q)):
                    word = q.popleft()

                    if word == endWord:
                        return transformations
                    for nei in adjMap[word]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                
                transformations += 1
            return 0

        return bfs()