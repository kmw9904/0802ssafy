def Selectionsort_1(arr, N):
    for i in range(N - 1):
        mn_ist = i
        for j in range(i + 1, N):
            if arr[mn_ist] > arr[j]:
                mn_ist = j

        arr[i], arr[mn_ist] = arr[mn_ist], arr[i]

    return arr

# def Selectionsort_1(arr, N):
#     for i in range(N - 1):
#         mn_ist = i
#         for j in range(i + 1, N):
#             if arr[mn_ist] > arr[j]:
#                 mn_ist = j
#         # 내부 루프가 끝난 후 교환을 수행해야 합니다.
#         arr[i], arr[mn_ist] = arr[mn_ist], arr[i]
#
#     return arr

a = [2, 7, 5, 3, 4]
b = [4, 3, 2, 1]
result2 = Selectionsort_1(a, len(a))
result3 = Selectionsort_1(b, len(b))
print(result2)
print(result3)
