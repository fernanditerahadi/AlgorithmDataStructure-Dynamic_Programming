# Uses python3
import math
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minandmax(i,j):
    minimum = +math.inf
    maximum = -math.inf
    for k in range(i,j):
        a = evalt(large_tab[i][k],large_tab[k+1][j],op[k])
        b = evalt(large_tab[i][k],small_tab[k+1][j],op[k])
        c = evalt(small_tab[i][k],large_tab[k+1][j],op[k])
        d = evalt(small_tab[i][k],small_tab[k+1][j],op[k])
        minimum = min(minimum, a,b,c,d)
        maximum = max(maximum, a,b,c,d)
    return minimum, maximum


def get_maximum_value(dataset):
    global small_tab, large_tab, op
    num = dataset[0:len(dataset):2]
    op = dataset[1:len(dataset):2]
    n = len(num)
    small_tab = [[0 for x in range(n)] for x in range(n)]
    large_tab = [[0 for x in range(n)] for x in range(n)]

    for x in range(0,n):
        small_tab[x][x] = int(num[x])
    for x in range(0,n):
        large_tab[x][x] = int(num[x])

    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            small_tab[i][j], large_tab[i][j] = minandmax(i,j)

    #for x in small_tab:
    #    print(x)
    #print('')
    #for x in large_tab:
    #    print(x)

    return large_tab[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
