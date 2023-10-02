def array_sum(a: list, b: list, k: int) -> bool:
    if len(a) != len(b):
        return False

    a.sort()
    b.sort(reverse=True)

    for i in range(len(a)):
        if (a[i] + b[i] < k):
            return False
        
    return True

a = [2, 1, 3]
b = [8, 9, 7]

print(array_sum(a, b, 10))