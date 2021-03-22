def count(a, b):
    return max((min(a//2, b)-1) + (min(a, b//2)-1), 0)

def grid(X, i, j):
    return X[i][j] if len(X) > len(X[0]) else X[j][i]

def l_shaped_plots():
    R, C = map(int, raw_input().strip().split())
    G = [map(int, raw_input().strip().split()) for _ in xrange(R)]

    result = 0
    for direction in (lambda x: x, reversed):
        dp = [0]*min(R, C)
        for i in direction(xrange(max(R, C))):
            for direction in (lambda x:x, reversed):
                curr = 0
                for j in direction(xrange(min(R, C))):
                    if not grid(G, i, j):
                        dp[j] = 0
                        curr = 0
                        continue
                    dp[j] += 1
                    curr += 1
                    result += count(curr, (dp[j]+1)//2)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, l_shaped_plots())
