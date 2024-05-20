def find_missing_number(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 1:
            return arr[i - 1] + 1
    return None
