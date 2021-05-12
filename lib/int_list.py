import sys


def get_mode(arr):
    k = len(arr)
    for i in range(0, k):
        arr[arr[i] % k] += k

    max = arr[0]
    result = 0
    for i in range(1, k):

        if arr[i] > max:
            max = arr[i]
            result = i

    return result


# [2, 4, 6, 10], 12
def num_subsets_add_to_k_memoized(nums, k):
    memo = {}

    def helper(nums, k, index):
        if (k, index) in memo:
            return memo[(k, index)]
        if k == 0:
            memo[(k, index)] = 1
        elif index < 0 or k < 0:
            memo[(k, index)] = 0
        elif k < nums[index]:
            memo[(k, index)] = helper(nums, k, index - 1)
        else:
            memo[(k, index)] = helper(nums, k - nums[index], index - 1) + helper(
                nums, k, index - 1
            )
        return memo[(k, index)]

    return helper(nums, k, len(nums) - 1)


def num_subsets_add_to_k(nums, k):
    combinations = [[]]
    for num in nums:
        for index in range(len(combinations)):
            cloned = list(combinations[index])
            combinations[index].append(num)
            combinations.append(cloned)
    return sum([1 if sum(combo) == k else 0 for combo in combinations])


# {1,2,3}, [4,3,2,6,1,7] => [3,2,6,1]
def shortest_continuous_subarray(int_set, random_ints):
    if not len(int_set) or not len(random_ints):
        return []
    best = sys.maxsize
    best_indices = []
    for start_index in range(len(random_ints)):
        ints_seen = set()
        for current_index in range(start_index, len(random_ints)):
            current_num = random_ints[current_index]
            if current_num in int_set:
                ints_seen.add(current_num)
                if len(ints_seen) == len(int_set):
                    best = min(best, current_index - start_index)
                    if current_index - start_index == best:
                        best_indices = [start_index, current_index]
                    break
    if not len(best_indices):
        return []
    return random_ints[best_indices[0] : best_indices[1] + 1]


def shortest_continuous_subarray_linear(int_set, random_ints):
    if not len(int_set) or not len(random_ints):
        return []
    best = sys.maxsize
    best_indices = []
    ints_seen = {}
    first_index = sys.maxsize
    last_index = -sys.maxsize
    for index in range(len(random_ints)):
        num = random_ints[index]
        if num in int_set:
            if index < first_index:
                first_index = index
            if index > last_index:
                last_index = index
            ints_seen[num] = index
            if len(int_set) == len(ints_seen):
                best = min(best, last_index - first_index)
                if last_index - first_index == best:
                    best_indices = [first_index, last_index]
    if not len(best_indices):
        return []
    return random_ints[best_indices[0] : best_indices[1] + 1]
