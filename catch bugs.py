import sys
sys.stdin = open('input/catach bugs.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            results = 0
            for k in range(M):
                for n in range(M):
                    results += lst[i + k][j + n]
            result.append(results)

    print(f'#{tc} {max(result)}')