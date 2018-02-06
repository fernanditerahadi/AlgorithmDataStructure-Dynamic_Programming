# Uses python3
def edit_distance(s, t):
    m = len(t) ; n = len(s)
    table = [[0 for x in range(m+1)] for x in range(n+1)]
    for x in range(0, n+1):
        table[x][0] = x
    for x in range(0, m+1):
        table[0][x] = x
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = table[i][j-1] + 1
            deletion = table[i-1][j] + 1
            if s[i-1] == t[j-1]:
                table[i][j] = min(insertion, deletion, table[i-1][j-1])
            else:
                table[i][j] = min(insertion, deletion, table[i-1][j-1] + 1)
    return table[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
