T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))
    mx_list_N = 0
    mn_list_N = 999999999999
    for k in range(0, N-M+1):
        sum_list = 0
        for j in range(M):
            sum_list += list_N[k+j]
        if sum_list > mx_list_N:
            mx_list_N = sum_list

        if sum_list < mn_list_N:
            mn_list_N = sum_list
    print(f'#{i} {mx_list_N - mn_list_N}')

