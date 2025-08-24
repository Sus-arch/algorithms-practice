import sys

mod = 10 ** 9 + 7
data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:1 + n]))

M = 1
f = 1
s0 = {}

for x in a:
    if x not in s0:
        s0[x] = 0
    s_x = (s0[x] * M) % mod
    f_old = f
    new = (f_old - s_x) % mod
    if new < 0:
        new += mod
    f = (f_old + new) % mod
    temp = 2 * M % mod
    inv2M = pow(temp, mod - 2, mod)
    s0[x] = (f_old * inv2M) % mod
    M = (2 * M) % mod

result = (f - 1) % mod
if result < 0:
    result += mod
print(result)