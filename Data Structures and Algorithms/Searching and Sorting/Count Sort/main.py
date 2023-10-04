def count_sort(array: list):
    maximum = max(array)
    positions = [0] * (maximum + 1)
    count_array = [0] * (maximum + 1)

    for i in array:
        count_array[i] += 1

    for i in range(1, len(count_array)):
        positions[i] = count_array[i] + positions[i-1]

    sorted_array = [0] * len(array)

    for i in array[::-1]:
        index = positions[i] - 1
        sorted_array[index] = i
        positions[i] -= 1

    return sorted_array

array = [1, 3, 2, 3, 4, 1, 6, 4, 3]
print(f"Array before sorting: {array}")

array = count_sort(array)
print("Algorithm Used: Count Sort", end = "\n")
print(f"Array after sorting: {array}")