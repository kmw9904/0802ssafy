import sys

sys.stdin = open('input (4).txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx_result = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            result = 0
            for k in range(M):
                for l in range(M):
                    result += arr[i + k][j + l]

            if mx_result < result:
                mx_result = result

    print(f'#{tc} {mx_result}')
