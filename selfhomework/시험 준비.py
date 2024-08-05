# 버블 정렬
def bubbleSort(arr, N):
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 카운팅 정렬
def couningsort(arr,N):
    temp = [0] * N
    count = [0] * 50000

    for i in arr:
        count[i] += 1

    for i in range(1, N):
        count[i] += count[i-1]

        for i in range(N-1,-1,-1):
            x = arr[i]
            count[x] -= 1
            temp[count[x]] = x

    return temp


arr1 = [5, 7, 43, 34, 7, 4, 4, 0, 34, 624, 345, 5654, 675, 345, 234, 5476, 67]
result = couningsort(arr1, len(arr1))
print(result)
