my_list = [1, 2, 3]

# Loop through the first half of the list
for i in range(len(my_list) // 2):
    # Calculate the corresponding index from the end of the list
    j = len(my_list) - 1 - i
    
    # Swap elements at indices i and j
    my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)