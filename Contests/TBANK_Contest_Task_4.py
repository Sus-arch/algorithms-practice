from collections import deque


def simulate_flow(n, l, r, a, start):
    tanks = [0] * n
    left_cap = l[:]
    right_cap = r[:]
    total_water = 0

    # Start by filling the initial tank
    queue = deque([(start, float('inf'))])
    visited = [False] * n
    visited[start] = True

    while queue:
        curr, path_flow = queue.popleft()

        can_store = min(path_flow, a[curr] - tanks[curr])
        tanks[curr] += can_store
        total_water += can_store

        if curr > 0 and left_cap[curr] > 0 and not visited[curr - 1]:
            flow = min(path_flow, left_cap[curr], a[curr - 1] - tanks[curr - 1])
            if flow > 0:
                left_cap[curr] -= flow
                visited[curr - 1] = True
                queue.append((curr - 1, flow))

        if curr < n - 1 and right_cap[curr] > 0 and not visited[curr + 1]:
            flow = min(path_flow, right_cap[curr], a[curr + 1] - tanks[curr + 1])
            if flow > 0:
                right_cap[curr] -= flow
                visited[curr + 1] = True
                queue.append((curr + 1, flow))

    return total_water


def max_water_in_tanks():
    n = int(input())
    l = [0] * n
    r = [0] * n
    a = [0] * n
    for i in range(n):
        l[i], r[i], a[i] = map(int, input().split())

    max_water = 0
    for start in range(n):
        water = simulate_flow(n, l, r, a, start)
        max_water = max(max_water, water)

    return max_water


print(max_water_in_tanks())