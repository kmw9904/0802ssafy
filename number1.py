T = int(input())

for i in range(1, T+1):
    N = int(input())
    N_len = str(input())
    result = 0

    for j in range(1, N+1):
        find_num = '1'*j
        if find_num in N_len:
            result = len(find_num)

    print(f'#{i} {result}')
