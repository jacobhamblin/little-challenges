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

def get_deepest_node_refactor(root):
    def increment(node_and_depth):
        node, depth = node_and_depth
        return (node, depth + 1)

    def helper(node):
        if not node.left and not node.right:
            return (node, 1)

        if not node.left:
            return increment(helper(node.right))
        elif not node.right:
            return increment(helper(node.left))

        return increment(max(
            helper(node.left),
            helper(node.right),
            key=lambda x: x[1],
        ))

    return helper(root)[0]
