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

def test_find_cycle():
    a_head = linked_lists.linked_list_from_list([7,3,10])
    a_head.next.next.set_next(a_head)
    helpers.expect_equal(linked_lists.find_cycle(a_head), True)
    another_head = linked_lists.linked_list_from_list([2,4,6,3,10])
    another_head.next.next.next.next.set_next(another_head.next.next)
    helpers.expect_equal(linked_lists.find_cycle(another_head), True)
    third_head = linked_lists.linked_list_from_list([1,3,1,2,3])
    helpers.expect_equal(linked_lists.find_cycle(third_head), False)
    just_a_head = linked_lists.linked_list_from_list([3])
    helpers.expect_equal(linked_lists.find_cycle(just_a_head), False)
    helpers.expect_equal(linked_lists.find_cycle(None), False)
