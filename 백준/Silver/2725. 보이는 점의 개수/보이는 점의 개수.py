def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
dp = [0] * 1001
dp[1] = 3

for i in range(2, 1001):
    co_prime_count = 0
    for j in range(1, i + 1):
        if i == j:
            continue
        if gcd(i, j) == 1:
            co_prime_count += 2
    dp[i] = dp[i - 1] + co_prime_count

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])
