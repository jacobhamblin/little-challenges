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
