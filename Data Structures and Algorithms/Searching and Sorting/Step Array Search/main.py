from math import floor

def step_array_search(array: list, k: int, x: int):
    i = 0
    diff = 0

    for i in range(len(array)):
            if(array[i] == x):
                return i
            elif(array[i] < x):
                diff = x - array[i]
                i = floor(diff / k)


array = [4,5,6,8,12,15,18,21]
k = 3
x = 12

print(step_array_search(array, k, x))