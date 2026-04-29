class TrieNode:

    def __init__(self):
        self.hMap = defaultdict(TrieNode) #Maps char to TrieNode
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        wordList = list(word)
        node = self.root
        for c in wordList:
            if c not in node.hMap:
                node.hMap[c] = TrieNode()
            node = node.hMap[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        wordList = list(word)
        node = self.root
        for c in wordList:
            if c not in node.hMap:
                return False
            node = node.hMap[c]
        if node.endOfWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        prefixList = list(prefix)
        node = self.root
        for c in prefixList:
            if c not in node.hMap:
                return False
            node = node.hMap[c]
        return True