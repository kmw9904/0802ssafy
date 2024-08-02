T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    count = 1
    k = 0
    ci, cj = 0, 0

    while count != N ** 2:
        D = (k % 4)
        arr[ci][cj] = count
        ni = ci + di[D]
        nj = cj + dj[D]
        count += 1
s
        print(ci, cj)

        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            k += 1
            ni = ci + di[D]
            nj = cj + dj[D]
            continue


        if arr[ni][nj] != 0:
            k += 1
            ni = ci + di[D]
            nj = cj + dj[D]
            continue

        ci, cj = ni, nj

        # ci, cj = ni, nj

    print(arr)
