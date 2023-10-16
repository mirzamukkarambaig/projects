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

def round(list: list, key, mode: str = 'ceil') -> int:
    low, high = binary_search(list, key)
    
    if mode == 'ceil':
        return list[low]
    elif mode == 'floor':
        return list[high]
    else:
        raise ValueError("Invalid mode. Choose 'ceil' or 'floor'.")



array = [1, 2, 8, 10, 10, 12, 19]
print(round(array, 9, 'floor'))
