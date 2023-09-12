my_list = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
n = len(my_list)
m = 7
my_list.sort()

minimum_difference = float("inf")

for i in range(n - m + 1):
    current_difference = my_list[i + m - 1] - my_list[i]
    minimum_difference = min(current_difference, minimum_difference)
 

print(f"Minimum Difference: {minimum_difference}")