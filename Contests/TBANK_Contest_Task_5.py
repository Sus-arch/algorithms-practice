MOD = 10**9 + 7

def solve():
    n, k = map(int, input().split())

    maxA = n + k
    fact = [1] * (maxA + 1)
    for i in range(1, maxA + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (maxA + 1)
    inv[maxA] = pow(fact[maxA], MOD - 2, MOD)
    for i in range(maxA, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    def C(a, b):
        if b < 0 or b > a:
            return 0
        return fact[a] * inv[b] % MOD * inv[a - b] % MOD

    dp_prev = [0] * (n + 1)
    dp_prev[0] = 1

    for i in range(1, n + 1):
        dp = [0] * (n + 1)
        for s in range(0, n + 1):
            if dp_prev[s] == 0:
                continue
            max_m = (n - s) // i
            for m in range(0, max_m + 1):
                add = dp_prev[s] * C(m + k - 1, k - 1)
                dp[s + m * i] = (dp[s + m * i] + add) % MOD
        dp_prev = dp

    print(dp_prev[n])

if __name__ == "__main__":
    solve()
