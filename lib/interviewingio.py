def unique_half_candies(arr):
    unique_candies = set(arr)
    return min(len(unique_candies), len(arr) // 2)
