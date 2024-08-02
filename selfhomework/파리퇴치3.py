T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    x_di = [-1, 1, -1, 1]
    x_dj = [-1, -1, 1, 1]
    mx_result = 0

    for i in range(N):
        for j in range(N):
            result = 0
            result += arr[i][j]
            result1 = 0
            result1 += arr[i][j]

            for k in range(4):
                for l in range(1, M):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        result += arr[ni][nj]
                    x_ni = i + x_di[k] * l
                    x_nj = j + x_dj[k] * l
                    if 0 <= x_ni < N and 0 <= x_nj < N:
                        result1 += arr[x_ni][x_nj]
            if mx_result < result:
                mx_result = result

            if mx_result < result1:
                mx_result = result1

    print(f'#{tc} {mx_result}')
