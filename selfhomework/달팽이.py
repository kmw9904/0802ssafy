T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    count = 1
    ci, cj = 0, 0
    M = 0
    arr[ci][cj] = count
    while count != N ** 2:

        ni = ci + di[M % 4]
        nj = cj + dj[M % 4]


        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            M += 1
            continue

        if arr[ni][nj] != 0:
            M += 1
            continue

        ci, cj = ni, nj
        count += 1
        arr[ci][cj] = count

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])