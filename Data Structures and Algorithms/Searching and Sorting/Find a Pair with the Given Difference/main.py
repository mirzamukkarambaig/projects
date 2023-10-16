def find_pairs(arr: list, n: int) -> set:
    result = set()
    arr_set = set(arr)  # Convert the list to a set for O(1) membership checks
    
    for i in arr:
        if (i + n) in arr_set:
            result.add((i, i + n))
    
    return result

arr = [1, 8, 30, 40, 100]
n = 70

print(find_pairs(arr, n))
