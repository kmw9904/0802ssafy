T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    is_answer = False

    for i in range(N):
        for j in range(N - M + 1):
            string = arr[i][j:j + M]
            if string == string[::-1]:
                result = ''.join(string)
                print(f'#{tc} {result}')
                is_answer = True
                break

            lst = []
            for k in range(M):
                if arr[k + j][i] == arr[M - k - j - 1][i]:
                    lst.append(arr[k + j][i])
                else:
                    lst = []
                    break
            if lst != []:
                is_answer = True
                result = ''.join(lst)
                print(f'#{tc} {result}')
                break
        if is_answer == True:
            break


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    is_answer = False

    # 가로 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            string = arr[i][j:j + M]
            if string == string[::-1]:
                result = ''.join(string)
                print(f'#{tc} {result}')
                is_answer = True
                break
        if is_answer:
            break

    # 세로 회문 찾기
    if not is_answer:
        for j in range(N):
            for i in range(N - M + 1):
                string = [arr[i + k][j] for k in range(M)]
                if string == string[::-1]:
                    result = ''.join(string)
                    print(f'#{tc} {result}')
                    is_answer = True
                    break
            if is_answer:
                break
