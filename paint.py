T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst_map = [[0] * 10 for _ in range(10)]
    result = 0
    for k in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        if color == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    lst_map[i][j] += 1
                    if lst_map[i][j] == 3:
                        result += 1

        if color == 2:
            for i in range(c1, r2+1):
                for j in range(c1, c2+1):
                    lst_map[i][j] += 2
                    if lst_map[i][j] == 3:
                        result += 1

    print(f'#{tc} {result}')
