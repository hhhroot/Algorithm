import sys

MIN = -sys.maxsize

n = int(input())
nums = list(map(int, input().split()))

dp = [MIN for i in range(n)]
dp[0] = nums[0]

# 이전값 + 현재값 / 현재값부터 재 시작하는 값을 비교
for i in range(1, n):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])

print(max(dp))
