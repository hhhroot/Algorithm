N = int(input())

cnt = 0

# 각 인덱스 계산으로 대각선 값을 구할 수 있음 (https://velog.io/@qweadzs/BOJ-9663-N-QueenPython)
# X+Y(/) / X-Y+N-1(\)

row = [0] * N
dia1 = [0] * (N * 2 - 1)
dia2 = [0] * (N * 2 - 1)


def n_queen(x):
    global cnt
    print(row, cnt)
    if x == N:
        cnt += 1
        return

    for y in range(N):  # y축 값
        if row[y] == 0 and dia1[x + y] == 0 and dia2[x - y + N - 1] == 0:
            # 놓고, 놓고, 놓고 ...
            row[y] = dia1[x + y] = dia2[x - y + N - 1] = 1
            n_queen(x + 1)
            # 재귀가 끝나면 방금 놨던 곳을 0으로 바꾸고 다음 for문으로 돌아가게 됨
            row[y] = dia1[x + y] = dia2[x - y + N - 1] = 0  # 다시 0으로 놓고 다음 재귀 시작


# x축은 그냥 넣어줌
for xn in range(N):
    row[xn] = dia1[xn] = dia2[N - xn - 1] = 1
    n_queen(1)
    row[xn] = dia1[xn] = dia2[N - xn - 1] = 0

print(cnt)
