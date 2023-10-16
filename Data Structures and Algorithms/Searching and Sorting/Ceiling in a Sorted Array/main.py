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
    
def ceil(list: list, key) -> int:
    low, high = binary_search(list, key)
    return list[low]

def floor(list: list, key) -> int:
    low, high = binary_search(list, key)
    return list[high]


array = [1, 2, 8, 10, 10, 12, 19]
print(floor(array, 9))
