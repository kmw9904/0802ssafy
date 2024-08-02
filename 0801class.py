# 정렬이 되어 있지 않은 배열(리스트)에서 원하는 값의 인덱스 찾기!
def sequentialSearch(arr, N, target):
    """
    정렬이 되어 있지 않은 배열에서 타겟(target)의 인덱스를 반환 (없으면 -1)
    :param arr: 정렬되어 있지 않은 배열
    :param N: 배열의 길이
    :param target: 내가 찾고자 하는 값
    :return: target의 인덱스 (없으면 -1)
    """
    for i in range(N):
        # if ...:
        #     break # else문의 코드블럭 실행X !
        # 내가 찾고자하는 target 값을 발견하면 해당 인덱스 반환
        if arr[i] == target:
            return i
    else:
        # 타겟 값을 찾지 못한 경우
        return -1


arr = [6, 4, 23, 12, 4, 6, 1, 2, 5, 0, 5]
result = sequentialSearch(arr, len(arr), 5)
print(result) # 8 : 5의 인덱스 위치는 8
result = sequentialSearch(arr, len(arr), 10)
print(result) # -1 : 10의 값이 없음
