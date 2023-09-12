def binary_search(list, key):
    start = 0
    end = len(list) - 1

    while(start <= end):
        mid = (start + end) // 2

        if(list[mid] == key):
            return mid
        elif(list[mid]>key):
            end = mid - 1
        else:
            start = mid + 1

    return -1

my_list = [0, 1, 2, 4, 5, 6, 7]
key = 1
result = binary_search(my_list, key)
print(result)