# 입력
T = 10

for tc in range(1, T+1):
    # 덤프 횟수 ( 옮길 수 있는 최대 횟수)
    K = int(input())
    # 리스트로 상자의 높이들 boxes (100개)
    boxes = list(map(int, input().split()))

# 로직
    for k in range(K):
        # 최고점을 가지고 있는 박스의 위치 (인덱스)
        mx_idx = 0
        mx = boxes[mx_idx]
        # 박스들을 순회하며 최고점을 갱신
        for i in range(100):
            if mx < boxes[i]:
                mx = boxes[i]
                mx_idx = i

        # 최저점을 가지고 있는 박스의 위치 (인덱스)
        mn_idx = 0
        mn = boxes[mn_idx]

        # 박스들을 순회하며 최저점을 갱신
        for i in range(100):
            if mn > boxes[i]:
                mn = boxes[i]
                mn_idx = i
        # 최고점에서 최저점으로 박스 1 옮기기
        boxes[mx_idx] -= 1
        boxes[mn_idx] += 1

# 출력
    result = max(boxes) - min(boxes)
    print(f'#{tc} {result}')