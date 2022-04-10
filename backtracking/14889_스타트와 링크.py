import sys

N = int(input())

members = [
    [*map(int, input().split())] for _ in range(N)
]

res = sys.maxsize

check = [False] * N


def calc_stat(c):
    team1, team2 = [], []
    score1, score2 = 0, 0

    for idx, p in enumerate(c):
        if p:
            team1.append(idx)
        else:
            team2.append(idx)

    for i in range(N // 2):
        for j in range(N // 2):
            if i == j:
                continue
            score1 += members[team1[i]][team1[j]]
            score2 += members[team2[i]][team2[j]]

    return abs(score1 - score2)


# n : start team에 들어간 수, idx : idx번 사람
def start_link(n, idx):
    global res
    if n == N // 2:
        res = min(res, calc_stat(check))
        return
    if idx == N - 1:
        return

    # idx가 start team 에 들어감 (True)
    check[idx] = True
    start_link(n + 1, idx + 1)
    check[idx] = False  # 빼줬으니까 n은 그대로 둠
    start_link(n, idx + 1)


start_link(0, 0)
print(res)