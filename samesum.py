T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    la = len(A)
    result = 0

    for i in range(1 << la):
        results = []
        for j in range(la):
            if i & (1 << j):
                results.append(A[j])
        if len(results) == N and sum(results) == K:
            result += 1

    print(f'#{tc} {result}')
