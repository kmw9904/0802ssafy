T = 10

for _ in range(10):
    # 테스트케이스 번호 tc
    tc = int(input())
    # 100x100 이차원배열 arr
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 로직
    mx_total = 0 # 합에 대한 최대값

    # 가로(ㅡ)를 먼저 순회
    for i in range(100):
        total = 0 # 가로에 있는 한 줄에 대한 값을 모두 누적
        for j in range(100):
            total += arr[i][j]
        # 한 행의 합과 현재 최대값과 비교하여 갱신
        if mx_total < total:
            mx_total = total

    # 세로(ㅣ)를 순회
    for j in range(100):
        total = 0
        for i in range(100):
            total += arr[i][j]
        if mx_total < total:
            mx_total = total

    # 대각선 정방향...
    total = 0
    # for i in range(100):
    #     for j in range(100):
    #         if i == j:
    #             total += arr[i][j]
    for i in range(100):
        total += arr[i][i]
    if mx_total < total:
        mx_total = total

    # 대각선 역방향
    total = 0
    for i in range(100):
        total += arr[i][100-i-1]
    if mx_total < total:
        mx_total = total

    # 출력
    print(f'#{tc} {mx_total}')

import sys

sys.stdin = open("input.txt")

# 입력
T = 10
for _ in range(10):
    # 테스트케이스 번호 tc
    tc = int(input())
    # 100x100 이차원배열 arr
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 로직
    mx_total = 0  # 합에 대한 최대값

    # 가로(ㅡ)를 순회
    for i in range(100):
        total = 0 # 가로에 있는 한 줄에 대한 값을 모두 누적
        for j in range(100):
            total += arr[i][j]
        # 한 행의 합과 현재 최대값과 비교하여 갱신
        mx_total = max(mx_total, total)

    # 대각선 정방향...
    total = 0
    for i in range(100):
        total += arr[i][i]
    mx_total = max(total, mx_total)

    # 전치행렬 만들기 (90도 뒤집기)
    arr = list(map(list, zip(*arr)))

    # 가로(ㅡ)를 순회
    for i in range(100):
        total = 0 # 가로에 있는 한 줄에 대한 값을 모두 누적
        for j in range(100):
            total += arr[i][j]
        # 한 행의 합과 현재 최대값과 비교하여 갱신
        mx_total = max(mx_total, total)
    # 대각선 정방향...
    total = 0
    for i in range(100):
        total += arr[i][i]
    mx_total = max(total, mx_total)

    # 출력
    print(f"#{tc} {mx_total}")
