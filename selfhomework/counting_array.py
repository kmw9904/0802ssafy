def counting(arr):
    N = len(arr)
    counts = [0]  * 101
    temp = [0] * N

    for i in arr:
        counts[i] += 1

    for j in range(1, N):
        counts[j] += counts[j - 1]


    for x in range(N - 1, -1, -1):
        y = arr[x]

        temp[counts[y]-1] = y
        counts[y] -= 1

    return temp


arr1 = [0, 4, 1, 3, 1, 2, 4, 1]
result = counting(arr1)
print(result)
