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
def num_subsets_add_to_k_dp(nums, k):
    memo = [1]
    for i in xrange(1, k + 1):
        num_combos = 0
        used = set()
        for num in nums:
            if (i - num) in used:
                continue
            prior = i - num
            if num is i: num_combos += 1
            elif prior > 0 and num < i:
                if prior is not num and memo[num]:
                    print('prior is not num memo[num]', i, num, prior, memo[num])
                    num_combos += memo[prior] 
                    used.add(num)
        memo.append(num_combos)
    print(memo)
    return memo[k]

def num_subsets_add_to_k(nums, k):
    combinations = [[]]
    for num in nums:
        for index in xrange(len(combinations)):
            cloned = list(combinations[index])
            combinations[index].append(num)
            combinations.append(cloned)
    return sum([1 if sum(combo) == k else 0 for combo in combinations])