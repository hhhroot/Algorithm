n = int(input())
nums = list(map(int, input().split()))
reverse_nums = nums[::-1]

dp = [[1 for _ in range(n)] for _ in range(2)]

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[0][i] = max(dp[0][i], dp[0][j]+1)
        if reverse_nums[j] < reverse_nums[i]:
            dp[1][i] = max(dp[1][i], dp[1][j]+1)

dp[1].reverse()

result = []
for i in range(n):
    result.append(dp[0][i] + dp[1][i] - 1)

print(max(result))