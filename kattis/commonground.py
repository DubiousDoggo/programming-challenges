from math import gcd

N, L, W = (int(x) for x in input().split())
teamP = tuple(tuple(int(x) for x in input().split()) for _ in range(N))
teamQ = tuple(tuple(int(x) for x in input().split()) for _ in range(N))

pground = 0
cground = 0
for ty in range(W,-1,-1):
    for tx in range(L+1):
        for px, py, pr in teamP:
            if abs(tx-px) + abs(ty-py) <= pr:
                pground += 1
                for qx, qy, qr in teamQ:
                    if abs(tx-qx) + abs(ty-qy) <= qr:
                        cground += 1
                        print('c', end=' ')
                        break
                else:
                    print('p', end=' ')
                break
        else:
            print('.', end=' ')
    print('')


print(cground, pground, sep='/')
g = gcd(pground, cground)
pground //= g
cground //= g
print(cground, pground, sep='/')
