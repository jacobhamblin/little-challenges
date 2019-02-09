class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def add_left(self, node):
        self.left = node
    def add_right(self, node):
        self.right = node


def node_count(node):
    if not node:
        return 0
    return 1 + node_count(node.left) + node_count(node.right)

def get_deepest_node(root):
    def helper(node, depth, depths):
        if not node.left and not node.right:
            depths.append((node, depth))
        if node.left:
            helper(node.left, depth + 1, depths)
        if node.right:
            helper(node.left, depth + 1, depths)
    depths = []
    helper(root, 0, depths)
    deepest = max(depths, key=lambda x: x[1])
    return deepest[0]
