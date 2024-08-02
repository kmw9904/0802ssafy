# 입력
T = 10

for tc in range(1, T + 1):
    # 덤프 횟수 (옮길 수 있는 최대 횟수)
    K = int(input())
    # 리스트로 상자의 높이들 boxes (100개)
    boxes = list(map(int, input().split())) # ['1', '23', '4' ...]'

    # 로직
    for _ in range(K):
        # 정렬 사용하기...!
        boxes.sort() # 오름차순 (최소 가장처음, 최대 마지막)
        if boxes[0] == boxes[-1]:
            break
        boxes[0] += 1 # 최소값
        boxes[-1] -= 1 # 최대값

    # 출력 (최고점과 최저점의 차이값을 출력)
    result = max(boxes) - min(boxes)
    print(f"#{tc} {result}")