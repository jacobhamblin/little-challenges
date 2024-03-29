class GraphNode:
    def __init__(self, value, connected_nodes=[]):
        self.value = value
        self.connected_nodes = connected_nodes

    def __str__(self):
        return "GraphNode-%s" % self.value

    def add_connection(self, node):
        if not node in self.connected_nodes:
            self.connected_nodes.append(node)
        if not self in node.connected_nodes:
            node.connected_nodes.append(self)


def generate_graph_from_dict(graph_dictionary):
    nodes = {}
    for key, value_list in graph_dictionary.items():
        nodes[key] = GraphNode(key, [])
        for graph_node_value in value_list:
            if not graph_node_value in nodes:
                nodes[graph_node_value] = GraphNode(graph_node_value)
    for key, value_list in graph_dictionary.items():
        for connected_node_value in value_list:
            nodes[key].add_connection(nodes[connected_node_value])
    return nodes


def make_unvisited_graph_dict_nodes(graph_dict):
    for key, _ in graph_dict.items():
        setattr(graph_dict[key], "visited", False)
    return graph_dict


def dfs(current, target):
    if current.value == target:
        return current
    for connected_node in current.connected_nodes:
        visited = getattr(connected_node, "visited", None)
        if visited:
            continue
        setattr(connected_node, "visited", True)
        recursed = dfs(connected_node, target)
        if recursed:
            return recursed


def _bfs(target, node_queue):
    node = node_queue[0]
    if node.value == target:
        return node
    setattr(node, "visited", True)
    for connected_node in node.connected_nodes:
        visited = getattr(connected_node, "visited", None)
        if not visited:
            node_queue.append(connected_node)
    recursed = _bfs(target, node_queue[1:])
    if recursed:
        return recursed


def bfs(current, target):
    return _bfs(target, [current])
