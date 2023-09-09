my_list = [7, 3, 2, 4, 9, 12, 56]
n = 7
m = 3

my_list.sort()

minimum_difference = float("inf")
for i in range(len(my_list) - m + 1):
    current_difference = my_list[i + m] - my_list[i]
    if (current_difference < minimum_difference):
        minimum_difference = current_difference
 

print(f"difference: {current_difference}")

    