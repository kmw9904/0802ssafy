T = int(input())

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 결과값 result_sum
    result_sum = 0

    for i in range(N):

        # 행 값을 추가 ex. 첫출 [0, 0, 1, 1, 1]
        result_1 = []

        # count_k가 3이면은 result_sum에 1추가
        count_j = 0

        for j in range(N):
            result_1.append(lst[i][j])

            # 만약 k == 1 이 오면 count_k에 +1
            if lst[i][j] == 1:
                count_j += 1
                # 만약 k ==  0 이 오면 count_k를 0으로 초기화
            elif lst[i][j] == 0:
                count_j = 0
                # 만약 count_k가 3초과이면 0으로 초기화

            # 만약 count_k가 3이면 result_sum에 1추가 하며 count_k 초기화
            if count_j == K:
                result_sum += 1
            elif count_j > K:
                result_sum -= 1
                count_j = 0

    for j in range(N):
        result_2 = []
        count_k = 0
        for i in range(N):
            result_2.append(lst[i][j])
            # 만약 k == 1 이 오면 count_k에 +1
            if lst[i][j] == 1:
                count_k += 1
                # 만약 k ==  0 이 오면 count_k를 0으로 초기화
            elif lst[i][j] == 0:
                count_k = 0
                # 만약 count_k가 3초과이면 0으로 초기화

                # 만약 count_k가 3이면 result_sum에 1추가 하며 count_k 초기화
            if count_k == K:
                result_sum += 1
            elif count_k > K:
                result_sum -= 1
                count_k = 0

    print(f'#{tc} {result_sum}')
