class Node:
    def __init__(self):
        self.isfile = False
        self.files = {}
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = Node()
        

    def ls(self, path: str) -> List[str]:
        t = self.root
        files = []
        if path != "/":
            d = path.split("/")
            for i in range(1,len(d)):
                t = t.files[d[i]]
            if t.isfile:
                files.append(d[-1])
                return files
        res_files = sorted(t.files.keys())
        return res_files

    def mkdir(self, path: str) -> None:
        t = self.root
        d = path.split("/")
        for i in range(1, len(d)):
            if d[i] not in t.files:
                t.files[d[i]] = Node()
            t = t.files[d[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        t = self.root
        d = filePath.split("/")
        for i in range(1, len(d) - 1):
            t = t.files[d[i]]
        if d[-1] not in t.files:
            t.files[d[-1]] = Node()
        t = t.files[d[-1]]
        t.isfile = True
        t.content += content

    def readContentFromFile(self, filePath: str) -> str:
        t = self.root
        d = filePath.split("/")
        for i in range(1, len(d) - 1):
            t = t.files[d[i]]
        return t.files[d[-1]].content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
