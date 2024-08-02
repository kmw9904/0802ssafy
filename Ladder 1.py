import sys

sys.stdin = open('input/ladder_input.txt')

T = 10

for tc in range(1, T+1):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]


    ci, cj = 99, arr[99].index(2)
    di = [0, 0, -1]
    dj = [-1, 1, 0]

    while ci != 0:
        for k in range(3):
            ni = ci + di[k]
            nj = cj + dj[k]

            if ni < 0 or ni >=100 or nj < 0 or nj >= 100:
                continue

            if arr[ni][nj] == 1:
                arr[ci][cj] = 2
                ci, cj = ni, nj
                break

    print(f'#{tc} {cj}')