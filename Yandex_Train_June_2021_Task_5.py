from math import ceil


k1, m, k2, p2, n2 = map(int, input().split())
if m * (p2 - 1) >= k2:
    p1 = -1
    n1 = -1
elif n2 != 1 and k2 != 1:
    aps_on_floor = ceil(k2 / n2) 
    p1 = ceil(k1 / (aps_on_floor * m))
    n1 = ceil((k1 - (aps_on_floor * m)) / aps_on_floor)
else:
    p1 = 0
    n1 = 1

print(p1, n1)