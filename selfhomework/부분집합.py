arr = [1, 2, 3, 4, 5, 6]
N = len(arr)

for i in range(1 << N):
    result = []
    for j in range(N):
        if i & (1 << j):
            result.append(arr[j])
    print(result)
