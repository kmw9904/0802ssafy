T = int(input())


for i in range(1, T+1):
    case_number = int(input())
    test_lst = list(map(int, input().split()))
    test_frq = [0] * 101
    for j in test_lst:
        test_frq[j] += 1

    mx = 0
    mx_index = 0
    for k in range(len(test_frq)):
        if test_frq[k] >= mx:
            mx = test_frq[k]
            mx_index = k

    print(f'#{i} {mx_index}')