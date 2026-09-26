import sys

def generarParentesis(Y, N, i, A, R, maxI):
    if i >= maxI:
        if A == 0:
            R.append((int(N, 2), Y))
    else:
        if A > 0:
            generarParentesis(Y+')', N+'0', i+1, A-1, R, maxI)
        generarParentesis(Y+'(', N+'1', i+1, A+1, R, maxI)

for Z in sys.stdin:
    D = int(Z.strip())
    R = []
    generarParentesis('', '', 0, 0, R, D*2)
    for C in sorted(R, key=lambda x: x[0], reverse=True):
        print(C[1])
