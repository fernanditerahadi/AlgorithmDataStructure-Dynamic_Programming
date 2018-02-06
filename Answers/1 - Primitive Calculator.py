# Uses python3
import sys

def optimal_sequence(n):
    k = n
    sequence = []
    parent_tab = [0,1,1,1]
    minop_tab = [0,1,1,1]
    for i in range(4,n+1):
        curr_parent = i - 1
        curr_minop = minop_tab[curr_parent] + 1
        if i % 2 == 0:
            parent = i // 2
            op = minop_tab[(parent)] + 1
            if op < curr_minop:
                curr_parent, curr_minop = parent, op
        if i % 3 == 0:
            parent = i // 3
            op = minop_tab[(parent)] + 1
            if op < curr_minop:
                curr_parent, curr_minop = parent, op
        minop_tab.append(curr_minop) ; parent_tab.append(curr_parent)
    while k > 1:
        sequence.append(k)
        k = parent_tab[k]
    sequence.append(1)
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
