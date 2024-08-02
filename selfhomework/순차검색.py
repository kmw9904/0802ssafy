def counting_number(arr, key):
    for i in arr:
        if i == key:
            return arr.index(i)


arr1 = [4, 9, 11, 23, 2, 19, 7]
key = 2
result = counting_number(arr1, key)
print(result)


# 정렬되었을 때

def counting_number2(arr, key):
    for x in arr:
        if x == key:
            return f'찾는 값의 위치는 {arr.index(x)} 입니다.'
        elif x > key:
            return f'찾는 값이 없습니다.'


arr2 = [2, 4, 7, 9, 11, 19, 23]
key1 = 11
key2 = 8

result1 = counting_number2(arr2,key1)
result2 = counting_number2(arr2,key2)
print(result1)
print(result2)
