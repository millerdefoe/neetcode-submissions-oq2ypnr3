# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                serial.append("N")
            else:
                serial.append(str(node.val))
                q.append(node.left)
                q.append(node.right)


        return ".".join(serial)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        serial = data.split(".")
        if serial[0] == "N":
            return None
        
        root = TreeNode(int(serial[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if serial[index] != "N":
                node.left = TreeNode(int(serial[index]))
                q.append(node.left)
            index += 1
            if serial[index] != "N":
                node.right = TreeNode(int(serial[index]))
                q.append(node.right)
            index += 1

        return root
