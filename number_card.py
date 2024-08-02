T = int(input())

for i in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))
    # 0에서 9까지 숫자가 적힌 N장이기 때문에
    card_lst = [0] * 10

    for k in ai:
        card_lst[k] += 1

    mx = 0
    mx_index = 0
    for j in range(len(card_lst)):
        if card_lst[j] >= mx:
            mx = card_lst[j]
            mx_index = j

    print(f'#{i} {mx_index} {mx}')
