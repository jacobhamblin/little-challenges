def get_combinations(value, coins, coin_counts, combinations):
    if value == 0:
        combinations.append(coin_counts)
    for index, coin in enumerate(coins):
        if (value / coin) >= 1:
            new_coin_counts = list(coin_counts)
            new_coin_counts[index] += 1
            new_value = value - coin
            get_combinations(new_value, coins, new_coin_counts, combinations)


def fewest_coins(value, coins):
    coin_counts = [0 for coin in coins]
    if value == 0:
        return coin_counts
    combinations = []
    get_combinations(value, coins, coin_counts, combinations)
    get_sum = lambda x, y: x + y
    counts = [reduce(get_sum, nums) for nums in combinations]
    return combinations[counts.index(min(counts))]
