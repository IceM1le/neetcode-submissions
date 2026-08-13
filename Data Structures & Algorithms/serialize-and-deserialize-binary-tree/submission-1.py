# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        if not data:
            return None
        tokens = iter(data.split(","))

        def build():
            val = next(tokens)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
