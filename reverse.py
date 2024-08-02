T = int(input())

for tc in range(1, T+1):
    word = input().strip()

    if word[::-1] == word :
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
