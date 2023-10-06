def find_common_in_three_arrays(ar1: list, ar2: list, ar3: list) -> list:
    common_list = find_common_elements(ar1, ar2)
    return find_common_elements(common_list, ar3)

def find_common_elements(ar1: list, ar2: list) -> list:
    common_elements = []
    i = 0
    j = 0

    while i < len(ar1) and j < len(ar2):
        if ar1[i] < ar2[j]:
            i += 1
        elif ar2[j] < ar1[i]:
            j += 1
        else:
            common_elements.append(ar1[i])
            i += 1
            j += 1

    return common_elements

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(find_common_in_three_arrays(ar1, ar2, ar3))
