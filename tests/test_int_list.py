from . import helpers
from lib import int_list


def test_get_mode():
    helpers.expect_equal(int_list.get_mode([1,2,3,2]), 2)
    helpers.expect_equal(
        int_list.get_mode([5,2,3,1,2,5,7,5,4]),
        5
    )
    helpers.expect_equal(
        int_list.get_mode([2,4,6,3,4,1]),
        4
    )

def test_num_subsets_add_to_k():
    expect = helpers.expect_equal
    function_names = ['num_subsets_add_to_k', 'num_subsets_add_to_k_memoized']
    for function_name in function_names:
        func = getattr(int_list, function_name)
        nums = [2, 4, 6, 10]
        expect(func(nums, 0), 1)
        expect(func(nums, 1), 0)
        expect(func(nums, 2), 1)
        expect(func(nums, 3), 0)
        expect(func(nums, 4), 1)
        expect(func(nums, 6), 2)
        expect(func(nums, 8), 1)
        expect(func(nums, 10), 2)
        expect(func(nums, 12), 2)
        expect(func(nums, 16), 2)