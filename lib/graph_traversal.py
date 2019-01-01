class GraphNode:
    def __init__(self, value, connected_nodes):
        self.value = value
        self.connected_nodes = connected_nodes
    def __str__(self):
        return 'GraphNode-%s' % self.value

    def add_connection(self, node):
        if not node in self.connected_nodes:
            self.connected_nodes.append(node)
        if not self in node.connected_nodes:
            node.connected_nodes.append(self)


def generate_graph_from_dict(graph_dictionary):
    nodes = {}
    for key, value in graph_dictionary.iteritems():
        nodes[key] = GraphNode(key, [])
    for key, value in graph_dictionary.iteritems():
        for connected_node_value in value:
            nodes[key].add_connection(nodes[connected_node_value])
    return nodes
