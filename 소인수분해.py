T = int(input())

'''
N은 아래와 같다.

N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.


[제약 사항]

N은 2 이상 10,000,000 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

for i in range(1, T+1):
    N = int(input())
    count_2 = 0
    count_3 = 0
    count_5 = 0
    count_7 = 0
    count_11 = 0
    while N % 2 == 0:
        N = N // 2
        count_2 += 1

    while N % 3 == 0:
        N = N // 3
        count_3 += 1

    while N % 5 == 0:
        N = N // 5
        count_5 += 1

    while N % 7 == 0:
        N = N // 7
        count_7 += 1

    while N % 11 == 0:
        N = N // 11
        count_11 += 1

    print(f'#{i} {count_2} {count_3} {count_5} {count_7} {count_11}')



