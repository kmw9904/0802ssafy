def binary_serach(arr, key):
    start = 0
    end_pnt = len(arr) - 1

    while start <= end_pnt:
        median = (start + end_pnt) // 2

        if arr[median] == key:
            return f'위치는 {median}입니다.'
        elif arr[median] > key:
            end_pnt = median - 1
        else:
            start = median + 1

    return '값을 찾을 수 없습니다.'

arr1 = [2,4,7,9,11,19,23]
key1 = 19
key2= 4
key3= 20
result1 = binary_serach(arr1,key1)
result2 = binary_serach(arr1,key2)
result3 = binary_serach(arr1,key3)
print(result1)
print(result2)
print(result3)