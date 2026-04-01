# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # we can do a pre-order traversal of the tree
        res = []

        def dfsToSerial(node):
            if not node:
                res.append("null")
                return 0

            res.append(str(node.val))
            dfsToSerial(node.left)
            dfsToSerial(node.right)
            return 0

        dfsToSerial(root)
        resJ = ".".join(res)

        return resJ
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataOut = data.split(".")
        self.i = 0



        def dfsToSerial():
            if dataOut[self.i] == "null":
                self.i += 1
                return None
            
            node = TreeNode(int(dataOut[self.i]))
            self.i += 1
            node.left = dfsToSerial()
            node.right = dfsToSerial()
            
            return node
        
        return dfsToSerial()

        

