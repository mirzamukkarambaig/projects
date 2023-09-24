def chocolate_distribution(list: list, m: int):
    list.sort()
    n = len(list)
    minimum_difference = float("inf")
    for i in range(n - m + 1):
        current_difference = list[i + m - 1] - list[i]
        minimum_difference = min(current_difference, minimum_difference)
    return minimum_difference


my_list = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
difference = chocolate_distribution(my_list, m)
print(f"Minimum Difference: {difference}")

