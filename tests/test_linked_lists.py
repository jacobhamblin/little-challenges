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

def test_merge_sorted_lists():
    expect = helpers.expect_equal
    func = linked_lists.merge_sorted_lists
    sorted_lists = [[3,7,10], [1,4,5], [1,3,6]]
    a_head = linked_lists.linked_list_from_list(sorted_lists[0])
    b_head = linked_lists.linked_list_from_list(sorted_lists[1])
    c_head = linked_lists.linked_list_from_list(sorted_lists[2])
    merged = func([a_head, b_head, c_head])
    vals = []
    while merged:
        vals.append(merged.value)
        merged = merged.next
    expect(vals, sorted([val for list in sorted_lists for val in list]))
