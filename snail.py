"""
델타탐색 : 특정 좌표를 기준으로 상대 좌표를 탐색하는 방


현재 좌표: (ci, cj)
방향전환 : 1. 배열 바깥으로 좌표가 나갈 때
          2. 배열에 이미 값이 있는 좌표로 갈 때
if ci < 0 or ci >= N or cj < 0 or cj >= N:
    pass # ?? 어떤 코드 써야지
if arr[ci][cj] != 0:
    pass # ?? 어떤 코드 써야지

달팽이가 지나간 공간에 숫자 쓰기! (사용한 숫자는 카운트+1)

반복 수행을 할 반복문 (조건???)
: 전체 이동(카운트 값)이 `N ** 2` 이 된다면 정지!
"""

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 입력
# 테스트 케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 이차원 배열의 한변의 길이 N
    N = int(input())
    # 이차원 배열을 생성 NxN arr
    arr = [[0 for _ in range(N)] for _ in range(N)]

    # 로직 (달팽이 이동 시작)
    # 달팽이에게 필요한 데이터??? (상태)
    i, j = 0, 0  # 달팽이 위치 좌표 (i, j)
    cnt = 1  # 달팽이가 찍어야할 수 (걸음수)
    k = 0  # 달팽이가 현재 진행하는 방향

    # 시작점을 먼저 찍어두고 시작!
    arr[i][j] = cnt

    # 반복문 (달팽이가 한 걸음씩 이동!)
    while cnt < N ** 2: # 종료조건 : N ** 2가 될때까지 이동!
        # 내가 이동하려는 좌표 (ni, nj), 방향 k
        ni = i + di[k]
        nj = j + dj[k]

        # 방향전환 : 1. 배열 바깥으로 좌표가 나갈 때
        #           2. 배열에 이미 값이 있는 좌표로 갈 때
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            k = (k + 1) % 4
            continue
        if arr[ni][nj] != 0:
            k = (k + 1) % 4
            continue

        # 해당 위치로 달팽이를 이동! (i, j) -> (ni, nj)
        i, j = ni, nj
        cnt += 1
        arr[i][j] = cnt


    # 출력
    print(f"#{tc}")
    for i in range(N):
        print(*arr[i])
