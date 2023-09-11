def search_in_rotated_array(arr, key, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == key:
        return mid

    # Check if the left half is normally sorted
    if arr[start] <= arr[mid]:
        if key >= arr[start] and key <= arr[mid]:
            return search_in_rotated_array(arr, key, start, mid - 1)
        else:
            return search_in_rotated_array(arr, key, mid + 1, end)

    # If the left half is not normally sorted, the right half must be
    if key >= arr[mid] and key <= arr[end]:
        return search_in_rotated_array(arr, key, mid + 1, end)
    else:
        return search_in_rotated_array(arr, key, start, mid - 1)


def search_rotated(arr, key):
    return search_in_rotated_array(arr, key, 0, len(arr) - 1)


my_list = [4, 5, 6, 7, 0, 1, 2]
result = search_rotated(my_list, 2)
print(result)
