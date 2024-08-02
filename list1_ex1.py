T = int(input())    # 테스트 케이스 수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for i in arr:
        if i > max_v:
            max_v = i
        elif i < min_v:
            min_v = i
    answer = max_v - min_v
    print(f'#{tc} {answer}')

