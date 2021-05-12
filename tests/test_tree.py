from . import helpers
from lib import tree


expect = helpers.expect_equal
Node = tree.Node


def provide_tree():
    root = Node(10)
    left = Node(5)
    root.add_left(left)
    right = Node(13)
    root.add_right(right)
    left_left = Node(3)
    root.left.add_left(left_left)
    left_right = Node(7)
    root.left.add_right(left_right)
    left_left_left = Node(1)
    root.left.left.add_left(left_left_left)
    return root


def test_node_count():
    root = provide_tree()
    expect(tree.node_count(root), 6)


def test_get_deepest_node():
    root = provide_tree()
    for func in [tree.get_deepest_node, tree.get_deepest_node_refactor]:
        expect(func(root).value, 1)
