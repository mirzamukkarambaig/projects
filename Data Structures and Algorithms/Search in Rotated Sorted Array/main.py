# element_to_find = 0

# if element_to_find in my_list:
#     index = my_list.index(element_to_find)
#     print(f"The element {element_to_find} is at index {index}.")
# else:
#     print(f"The element {element_to_find} is not in the list.")

def binary_search(list, key):
    start = 0
    end = len(list) - 1

    while(start <= end):
        mid = int((start + end) / 2)

        if(list[mid] == key):
            return mid
        elif(list[mid]>key):
            end = mid - 1
        else:
            start = mid + 1

    return -1


my_list = [0,1,2,4,5,6,7]
result = binary_search(my_list, 2)
print(result)