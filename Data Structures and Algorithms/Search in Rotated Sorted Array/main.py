my_list = [0,1,2,4,5,6,7]
n = 3

for i in range(n):
    element = my_list.pop(0)
    my_list.append(element)

element_to_find = 0

if element_to_find in my_list:
    index = my_list.index(element_to_find)
    print(f"The element {element_to_find} is at index {index}.")
else:
    print(f"The element {element_to_find} is not in the list.")