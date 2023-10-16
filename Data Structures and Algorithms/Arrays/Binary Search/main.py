from typing import List

def binary_search(values: List[int], key: int) -> int:
    """
    Performs a binary search for the given key in the sorted list.
    If key is found, returns its index.
    If key is not found, returns the indices where the key should be inserted (low and high).
    """
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2

        if values[mid] == key:
            return mid
        elif values[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1

my_list = [0, 1, 2, 4, 5, 6, 7]
key = 1
result = binary_search(my_list, key)
print(result)