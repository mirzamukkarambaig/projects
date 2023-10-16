def binary_search(list, key):
    low = 0
    high = len(list) - 1

    while(low <= high):
        mid = (low + high) // 2

        if(list[mid] == key):
            return mid
        elif(list[mid]>key):
            high = mid - 1
        else:
            low = mid + 1

    return low, high

def round(list: list, key, mode: bool = True) -> int:
    # True -> Ceil, False -> floor
    low, high = binary_search(list, key)
    
    if mode:
        return list[low]
    else:
        return list[high]


array = [1, 2, 8, 10, 10, 12, 19]
print(round(array, 9, False))
