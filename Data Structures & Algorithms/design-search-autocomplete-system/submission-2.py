from collections import defaultdict
import heapq

class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = defaultdict(TrieNode)
        self.times = 0


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # initialise a trie, this our prefix matcher
        # in a trie the endnode will have an "endOfWord", "access counter += if its an endOfWord"
        # trie node, End of Word value and a dicitionary mapping to other trie nodes
        # make a subfunction to ingest into the trie so input and __init__ will call it
        # input will ingest the trie upon a # with a use of 1.
        self.trieRoot = TrieNode()
        for sentence, time in zip(sentences, times):
            self.insertIntoTrie(self.trieRoot, sentence, time)
        self.buffer = []

    def insertIntoTrie(self, root: TrieNode, s: str, t: int):
        # to insert, check the dictionary if it exists continue else, add a entry. 
        # once we hit the end of word, EoW = True
        node = root
        sList = list(s)
        for char in sList:
            node = node.children[char]
        node.endOfWord = True
        node.times += t


    def input(self, c: str) -> List[str]:
        if c == "#": #flush the buffer and append to Trie
            self.insertIntoTrie(self.trieRoot, self.buffer, 1)
            self.buffer = []
            return []

        self.buffer.append(c)
        # finding the start point of our DFS
        node = self.trieRoot
        for char in self.buffer:
            if char not in node.children:
                return []
            node = node.children[char]
        #now we have the starting point of dfs if valid
        maxHeap = []
        #maxHeap will take in (-times, sentence)
        
        def dfs(node, word):
            if node.endOfWord:
                heapq.heappush(maxHeap, (-node.times, word))
            
            for char in node.children.keys():
                dfs(node.children[char], word + char)
            
            return

        dfs(node, ''.join(self.buffer))
        print(f'{maxHeap=}')
        result = []
        while maxHeap and len(result) < 3:
            result.append(heapq.heappop(maxHeap)[1])
        return result
        #maxHeap in here to get top 3. if len(maxHeap) < 3: return the whole thing


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
