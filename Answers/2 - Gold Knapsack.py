#Uses Python3
import sys
def optimal_weight(W, w):
    bag = [0] * (W+1)
    for i in range(len(w)):
        for j in range(W, w[i]-1, -1):
            bag[j] = max(bag[j], bag[j - w[i]] + w[i])
    return bag[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
