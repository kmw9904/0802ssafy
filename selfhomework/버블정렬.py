def bubble_sort(arr):
    N = len(arr)
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return  arr
arr = [9,8,7,6,5,4,3,2,1]
result = bubble_sort(arr)
print(result)