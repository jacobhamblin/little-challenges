from lib import linked_lists
from . import helpers


def test_two_lists():
    first_list = linked_lists.linked_list_from_list([3,5,7,8,10])
    second_list = linked_lists.linked_list_from_list([2,4,6,8,10])

    helpers.expect_equal(
        linked_lists.common_node(first_list, second_list),
        8
    )


def test_two_lists_varying_length():
    first_list = linked_lists.linked_list_from_list([7,3,10])
    second_list = linked_lists.linked_list_from_list([2,4,6,3,10])

    helpers.expect_equal(
        linked_lists.common_node(first_list, second_list),
        3
    )
