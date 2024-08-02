# 선택 정렬 알고리즘
def selectionSort(arr, N):
    # for i : 0 ~ n -2
    #   a[i]....a[n-1] 원소에 최솟값을 찾는다.
    #   a[i] <-> a[k] 요소를 교환
    for i in range(N - 1):
        mn_idx = i
        for j in range(i + 1, N):
            if arr[mn_idx] > arr[j]:
                mn_idx = j

        arr[i], arr[mn_idx] = arr[mn_idx], arr[i]


arr = [12, 33, 34, 534, 5, 23, 42, 3, 54, 776, 9, 90, 5, 6, 34, 52, 34, 13, 43, 57, 578]
selectionSort(arr, len(arr))
print(arr)
