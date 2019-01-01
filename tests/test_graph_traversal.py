from . import helpers
from lib import graph_traversal


functions = ['dfs']


def test_graph_from_dict():
    test_graph = {1: [2,3], 2: [1,3,4], 3: [1, 2], 4: [2]}
    test_graph = graph_traversal.generate_graph_from_dict(test_graph)
    helpers.expect_equal(test_graph[4].connected_nodes[0], test_graph[2])
    helpers.expect_equal(
        test_graph[1].connected_nodes,
        [test_graph[2], test_graph[3]]
    )
    helpers.expect_equal(
        test_graph[2].connected_nodes,
        [test_graph[1], test_graph[3], test_graph[4]]
    )
