import sys

sys.stdin = open('input (4).txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 1, -1, -1, -1, 0, 1]
    dj = [1, 0, 1, -1, 0, 1, -1, -1]
    mx_result = 0

    for i in range(N):
        for j in range(N):
            result = 0
            result += arr[i][j]

            if M == 2:
                for z in range(3):
                    ni = i + di[z]
                    nj = j + dj[z]

                    if 0 <= ni < N and 0 <= nj < N:
                        result += arr[ni][nj]
            else:
                for k in range(8):
                    for g in range(1, M):
                        ni = i + di[k] * g
                        nj = j + dj[k] * g
                        if 0 <= ni < N and 0 <= nj < N:
                            result += arr[ni][nj]

            if mx_result < result:
                mx_result = result

    print(f'#{tc} {mx_result}')
