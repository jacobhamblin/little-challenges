def get_mode(arr):
    k = len(arr)
    for i in range(0, k):
        arr[arr[i]%k] += k

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
            memo[(k, index)] = (
                helper(nums, k - nums[index], index - 1) + 
                helper(nums, k, index - 1)
            )
        return memo[(k, index)]
    return helper(nums, k, len(nums) - 1)

def num_subsets_add_to_k(nums, k):
    combinations = [[]]
    for num in nums:
        for index in xrange(len(combinations)):
            cloned = list(combinations[index])
            combinations[index].append(num)
            combinations.append(cloned)
    return sum([1 if sum(combo) == k else 0 for combo in combinations])