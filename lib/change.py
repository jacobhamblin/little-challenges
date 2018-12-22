def get_combinations(value, coins, coins_used, combinations):
    if value == 0:
        return coins_used
    for index, coin in enumerate(coins):
        if (value / coin) >= 1:
            cloned_coins_used = list(coins_used)
            cloned_coins_used[index] += 1
            result = get_combinations(
                value - coin,
                coins,
                cloned_coins_used,
                combinations
            )
            if result:
                combinations.append(result)


def fewest_coins(value, coins):
    coins_used = [0 for coin in coins]
    combinations = []
    get_combinations(value, coins, coins_used, combinations)
    if not len(combinations) or not len(combinations[0]):
        return coins_used
    sum = lambda x, y: x + y
    sums = [reduce(sum, combination) for combination in combinations]
    minimum_count = min(sums)
    for index, sum in enumerate(sums):
        if (sum) == minimum_count:
            return combinations[index]
