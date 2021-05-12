class LinkedListNode:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

    def set_next(self, next_node):
        self.next = next_node


def linked_list_from_list(list):
    if not len(list):
        return None
    list_of_nodes = []
    for item in list:
        list_of_nodes.append(LinkedListNode(item, None))
    for index, item in enumerate(list_of_nodes):
        if index != 0:
            list_of_nodes[index - 1].set_next(item)
    return list_of_nodes[0]


def common_node(first_node, second_node):
    first_length = 1
    second_length = 1
    node = first_node
    while node.next:
        first_length += 1
        node = node.next
    node = second_node
    while node.next:
        second_length += 1
        node = node.next
    if first_length > second_length:
        greater_length = first_length
        lesser_length = second_length
        node = first_node
        other_node = second_node
    else:
        greater_length = second_length
        lesser_length = first_length
        node = second_node
        other_node = first_node
    while greater_length > lesser_length:
        node = node.next
        greater_length -= 1
    while node.next:
        if node.value == other_node.value:
            return node.value
        node = node.next
        other_node = other_node.next
    return None


def find_cycle(head):
    if not head or not head.next:
        return False
    tortoise = head
    hare = head
    while hare.next and hare.next.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return True
    return False


def merge_sorted_lists(linked_lists):
    sorted_nodes = []
    if not linked_lists:
        return sorted_nodes
    while any(linked_lists):
        minimum = [0, 999999999999]
        list_index = 0
        while list_index < len(linked_lists):
            linked_list = linked_lists[list_index]
            if linked_list and linked_list.value < minimum[1]:
                minimum[1] = linked_list.value
                minimum[0] = list_index
            list_index += 1
        sorted_nodes.append(linked_lists[minimum[0]])
        linked_lists[minimum[0]] = linked_lists[minimum[0]].next
        if len(sorted_nodes) != 1:
            sorted_nodes[-2].next = sorted_nodes[-1]
    if not len(sorted_nodes):
        return sorted_nodes
    return sorted_nodes[0]
