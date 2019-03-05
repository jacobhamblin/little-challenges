from . import helpers
from lib import int_list

expect = helpers.expect_equal

def test_get_mode():
    expect(int_list.get_mode([1,2,3,2]), 2)
    expect(int_list.get_mode([5,2,3,1,2,5,7,5,4]), 5)
    expect(int_list.get_mode([2,4,6,3,4,1]), 4)

def test_num_subsets_add_to_k():
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

def test_shortest_continuous_subarray():
    function_names = ['shortest_continuous_subarray', 'shortest_continuous_subarray_linear']
    for function_name in function_names:
        func = getattr(int_list, function_name)
        expect(func({1,2,3}, [4,2,6,3,1,8]), [2,6,3,1])
        expect(func({1,2}, [4,2,6,3,1,8,3,4,1,3,2,0,0,1]), [1,3,2])
        expect(func({1,2,3,4}, [3,5,7,1,8,2,3]), [])
    
