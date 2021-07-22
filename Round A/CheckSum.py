#checkSum Problem Solution
def max_spanning_forest_prim(adj, n):  # Time: O(N^2), Space: O(N)
    result = 0
    max_e = [0]*len(n)
    lookup = [False]*len(n)
    for _ in xrange(len(n)):
        u = -1
        for v in xrange(len(n)):
            if lookup[v]:
                continue
            if u == -1 or max_e[v] > max_e[u]:
                u = v
        lookup[u] = True
        result += max_e[u]
        for v in xrange(len(n)):
            if adj[n[u]][n[v]] > max_e[v]:
                max_e[v] = adj[n[u]][n[v]]
    return result

def checksum():
    N = input()
    A = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    B = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    R = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())

    total = 0
    adj = [[0]*(2*N) for _ in xrange(2*N)]
    nodes = set()
    for i in xrange(len(A)):
        for j in xrange(len(A[0])):
            if A[i][j] != -1:
                continue
            adj[i][j+N] = adj[N+j][i] = B[i][j]  # Space: O(N^2)
            nodes.add(i)
            nodes.add(j+N)
            total += B[i][j]
    return total - max_spanning_forest_prim(adj, list(nodes))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, checksum())
