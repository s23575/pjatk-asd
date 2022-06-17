def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for i in range(m+1)] for j in range(n+1)]
    b = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, m):
        for j in range (1, n):
            print("X: ", i, j, "Y: ", i, j)
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = c[i-1][j-1]
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = c[i][j-1]
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = b[i-1][j]
    return c

# a = list("GTACTCAGTC")
# b = list("TCCAGTAATC")
a = list("ABCBDAB")
b = list("BDCABA")
print(lcs_length(a, b))