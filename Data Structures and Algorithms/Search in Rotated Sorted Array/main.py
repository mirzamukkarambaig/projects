def search_in_rotated_array(arr, key, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == key:
        return mid

    # Check if the left half is normally sorted
    if arr[left] <= arr[mid]:
        if key >= arr[left] and key <= arr[mid]:
            return search_in_rotated_array(arr, key, left, mid - 1)
        else:
            return search_in_rotated_array(arr, key, mid + 1, right)

    # If the left half is not normally sorted, the right half must be
    if key >= arr[mid] and key <= arr[right]:
        return search_in_rotated_array(arr, key, mid + 1, right)
    else:
        return search_in_rotated_array(arr, key, left, mid - 1)

my_list = [4, 5, 6, 7, 0, 1, 2]
key = 1
list_length = len(my_list)
result = search_in_rotated_array(my_list, key, 0, list_length - 1)
print(result)
