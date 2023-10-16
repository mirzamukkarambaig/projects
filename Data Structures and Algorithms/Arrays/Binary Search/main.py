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

    return -1

my_list = [0, 1, 2, 4, 5, 6, 7]
key = 1
result = binary_search(my_list, key)
print(result)