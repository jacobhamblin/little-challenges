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


def test_graph_from_dict_less_duplication():
    test_graph = {7: [3, 11], 3: [1,5], 11: [9, 13]}
    test_graph = graph_traversal.generate_graph_from_dict(test_graph)
    helpers.expect_equal(test_graph[7].connected_nodes[0], test_graph[3])
    helpers.expect_equal(
        test_graph[3].connected_nodes,
        [test_graph[1], test_graph[5], test_graph[7]]
    )


def test_no_loop():
    graph = {10: [5, 15], 5: [3,8], 15: [13, 18]}
    graph = graph_traversal.generate_graph_from_dict(graph)
    starts_and_targets = [
        [10, 13],
        [5, 8],
        [10, 8],
        [10, 10],
    ]
    for function_name in functions:
        function = getattr(graph_traversal, function_name)
        for start_and_target in starts_and_targets:
            graph = graph_traversal.make_unvisited_graph_dict_nodes(graph)
            helpers.expect_equal(
                function(graph[start_and_target[0]], start_and_target[1]),
                graph[start_and_target[1]],
            )
    graph = {6: [3, 9], 3: [1, 5]}
    graph = graph_traversal.generate_graph_from_dict(graph)
    starts_and_targets = [
        [6, 1],
        [6, 9],
        [3, 5],
        [5, 5],
    ]
    for function_name in functions:
        function = getattr(graph_traversal, function_name)
        for start_and_target in starts_and_targets:
            graph = graph_traversal.make_unvisited_graph_dict_nodes(graph)
            helpers.expect_equal(
                function(graph[start_and_target[0]], start_and_target[1]),
                graph[start_and_target[1]],
            )


def test_with_loops():
    graph = {10: [5, 15], 5: [3,8], 15: [13, 18], 13: [5, 15]}
    graph = graph_traversal.generate_graph_from_dict(graph)
    starts_and_targets = [
        [10, 13],
        [5, 8],
        [10, 8],
        [10, 10],
    ]
    for function_name in functions:
        function = getattr(graph_traversal, function_name)
        for start_and_target in starts_and_targets:
            graph = graph_traversal.make_unvisited_graph_dict_nodes(graph)
            helpers.expect_equal(
                function(graph[start_and_target[0]], start_and_target[1]),
                graph[start_and_target[1]],
            )
    graph = {6: [3, 9], 3: [1, 9, 5]}
    graph = graph_traversal.generate_graph_from_dict(graph)
    starts_and_targets = [
        [6, 1],
        [6, 9],
        [3, 5],
        [5, 5],
    ]
    for function_name in functions:
        function = getattr(graph_traversal, function_name)
        for start_and_target in starts_and_targets:
            graph = graph_traversal.make_unvisited_graph_dict_nodes(graph)
            helpers.expect_equal(
                function(graph[start_and_target[0]], start_and_target[1]),
                graph[start_and_target[1]],
            )
