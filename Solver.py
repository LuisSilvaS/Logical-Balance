#Calculando o Número mínimo de Pesagens

import math
 
def solve(N):
    if (N == 0):
        return 0
    if (N == 1):
        return 0
    rec = N
    return (solve(math.ceil(rec / 3.0)) + 1)
 
N = 9
print(solve(N))