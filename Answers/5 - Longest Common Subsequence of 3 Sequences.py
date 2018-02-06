#Uses python3
import sys

def lcs3(a, b, c):
    m, n, o = len(a), len(b), len(c)
    table = [[[None for x in range(o+1)] for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    table[i][j][k] = 0
                elif (a[i-1] == b[j-1] and a[i-1] == c[k-1]):
                    table[i][j][k] = table[i-1][j-1][k-1] + 1
                else:
                    table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k],
                                        table[i][j][k-1], table[i-1][j-1][k],
                                        table[i-1][j][k-1], table[i][j-1][k-1])

    return table[-1][-1][-1]
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
