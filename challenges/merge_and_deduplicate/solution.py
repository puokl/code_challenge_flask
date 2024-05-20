def merge_and_deduplicate(arr1, arr2):
    merged_array = arr1 + arr2
    return list(dict.fromkeys(merged_array))
