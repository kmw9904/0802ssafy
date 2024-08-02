# text = "1, 2, 3, 4, 5"  # input()  # "1, 2, 3, 4, 5" -> [1, 2, 3, 4, 5]
#
# arr = list(map(int, input().text.split()))
#
# # '12345' -> [1, 2, 3, 4, 5]
#
# arr2 = list(map(int, input()))
#
# # '1 2' -> ['1', '2'] -> map<[1, 2]> -> [1, 2] -> N,M = [1, 2]
# N, M = list(map(int, input().split()))
#
# pass

# def bubble_sort(lst):
#     # 요소의 개수 N
#     N = len(lst)
#     # i : N-1 -> 1, 마지막 범위
#     for i in range(N-1, 0, -1):
#         # j : [0, i) = 0은 포함되는데 j는 포함이 안되는 표현법
#         for j in range(0, i):
#             # 인접한 요소를 비교 후 교환
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#
# arr = [9,8,7,6,5,4,3,2,1]
# print(bubble_sort(arr))

# 카운트 배열 : 해당 수 (인덱스)의 빈도를 저장한 배열
# 0 <= x <= 100

# 카운트 배열에 카운트(빈도수)를 누적
for i in arr: # 요소를 하나씩 i를 가져오기
    counts[i] += 1

print(counts)






# 해당 요소(x)를 빈도수(seq) 만큼 출력해주면 되지롱!
for x in range(0, 11):
    seq = counts[x]
    # 빈도수 만큼 반복 수행
    for _ in range(seq):
        print(x, end=' ')
# 왜 이렇게 안하냐면 원본에 대한 순서를 보장해야 하는 경우가 필요하기 때문

def counting_sor(arr):
    N = len(arr)
    # 카운팅 배열 (초기화)
    counts = [0] * 101

    # 1. arr 배열을 순회하면서 카운트 진행
    for x in arr:
        counts[x] += 1

    # 2. 카운트 배열을 누적합으로 만들어주기
    # for i : 1 -> N - 1
    for i in range(1, N):
        counts[i] += counts[i-1]

    # 3. (정렬) 원본 배열을 역순으로 순회하면서 정렬 진행!
    #   저장해야할 필요가 있다면 임시 배열을 원본 배열 크기 만큼
    temp = [0] * N
    for i in range(N-1, -1, -1):
        x = arr[i] # 요소 하나 가져오기
        # 누적합 배열에 해당 인덱스를 1 감소
        counts[x] -= 1
        # 누적합 배열의 값을 가지고 해당 위치(인덱스)에 x 요소를 저장
        temp[counts[x]] = x
        # 위에꺼 풀어서 쓰면
        # j = counts[x]
        # temp[j] = x

    return temp