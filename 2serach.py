# 입력
T = int(input())

for tc in range(1,T+1):
    P, A, B = list(map(int, input().split()))

# 로직
    # A의 이진탐색
    start = 1
    result = 0

    while P <= A:
        c = int((P + start) / 2)
        result += 1
        if c == P:
            break
        elif c < P:
            start = c
        else:
            A = c

    # B의 이진탐색

    start = 1
    result_B = 0

    while P <= B:
        c = int((P + start) / 2)
        result_B += 1
        if c == P:
            break
        elif c < P:
            start = c
        else:
            B = c

    print(

        result, result_B)