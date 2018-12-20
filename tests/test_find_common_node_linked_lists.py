from lib import find_common_node_linked_lists
from . import helpers 


def test_two_lists():
    first_list = find_common_node_linked_lists.linked_list_from_list([3,5,7,8,10])
    second_list = find_common_node_linked_lists.linked_list_from_list([2,4,6,8,10])

    helpers.expect_equal(
        find_common_node_linked_lists.common_node(first_list, second_list),
        8
    )


def test_two_lists_varying_length():
    first_list = find_common_node_linked_lists.linked_list_from_list([7,3,10])
    second_list = find_common_node_linked_lists.linked_list_from_list([2,4,6,3,10])

    helpers.expect_equal(
        find_common_node_linked_lists.common_node(first_list, second_list),
        3
    )
