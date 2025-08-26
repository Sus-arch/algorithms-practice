import sys

def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    edges = []
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    seen = [False] * n
    for s in range(n):
        if not seen[s]:
            stack = [s]
            seen[s] = True
            ec = 0
            while stack:
                u = stack.pop()
                for v, _ in adj[u]:
                    ec += 1
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
            if (ec // 2) % 2 == 1:
                print(-1)
                return

    used_edge = [False] * m
    visited = [False] * n
    par = [0] * n
    ans = [None] * m

    def dfs(u: int):
        visited[u] = True
        for v, ei in adj[u]:
            if used_edge[ei]:
                continue
            used_edge[ei] = True
            if not visited[v]:
                dfs(v)
                if par[v] == 1:
                    ans[ei] = (v, u)
                    par[v] ^= 1
                else:
                    ans[ei] = (u, v)
                    par[u] ^= 1
            else:
                ans[ei] = (u, v)
                par[u] ^= 1

    for s in range(n):
        if not visited[s]:
            dfs(s)
            if par[s] == 1:
                print(-1)
                return

    out = []
    for u, v in ans:
        out.append(f"{u+1} {v+1}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
