for i in range(1, 11):
    T = int(input())
    N = list(map(int, input().split()))
    rlt_sum = 0
    for j in range(2, T-2):
        mxs = []
        for k in range(1, 3):
            mxs.append(N[j-k])
            mxs.append(N[j+k])
            mxs_max = 0
        for maxs in mxs:
            if maxs > mxs_max:
                mxs_max = maxs
        if mxs_max < N[j]:
            result = N[j] - mxs_max
            rlt_sum = rlt_sum + result
    print(f'#{i} {rlt_sum}')