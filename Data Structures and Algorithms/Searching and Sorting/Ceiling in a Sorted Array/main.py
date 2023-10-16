from typing import List

from typing import List, Tuple

def binary_search(values: List[int], key: int) -> Tuple[int, int]:
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

    return low, high

    
def ceil(values: List[int], key: int) -> int:
    """
    Returns the ceiling value for the given key from the sorted list.
    """
    low, high = binary_search(values, key)
    return values[low]

def floor(values: List[int], key: int) -> int:
    """
    Returns the floor value for the given key from the sorted list.
    """
    low, high = binary_search(values, key)
    return values[high]



array = [1, 2, 8, 10, 10, 12, 19]
print(floor(array, 9))
