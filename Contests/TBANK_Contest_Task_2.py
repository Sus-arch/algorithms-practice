import sys


data = sys.stdin.read().split()
t = int(data[0])
index = 1
results = []
for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n

    a.sort()
    valid = True
    for i in range(n):
        if a[i] > i + 1:
            valid = False
            break

    if not valid:
        results.append("Second")
    else:
        total_sum = sum(a)
        max_sum = n * (n + 1) // 2
        T = max_sum - total_sum
        if T % 2 == 1:
            results.append("First")
        else:
            results.append("Second")

for res in results:
    print(res)