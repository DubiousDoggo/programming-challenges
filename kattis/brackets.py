
def isValid(brac, l, r):
    n = 0
    for i in range(len(brac)):
        if l <= i and i <= r:
            if brac[i] == ')':
                n += 1
            else:
                n -= 1
        else:
            if brac[i] == '(':
                n += 1
            else:
                n -= 1
        if n < 0:
            return False
    return n == 0

def test(brac):
    if len(brac) & 1 != 0:
        return False

    if brac[0] == ')' and brac[-1] == '(':
        n = 0
        for k in brac:
            if k == ')':
                n += 1
            else:
                n -= 1
            if n < 0:
                return False
        return n == 0

    b = [None]*len(brac)
    n = 0
    for i in range(len(brac)):
        if brac[i] == '(':
            n += 1
        else:
            n -= 1
        b[i] = n

    lmax = len(b)-1
    for n in range(len(b)):
        if b[n] > len(b)-n:
            lmax = n   
            break
    print(lmax)

    if brac[-1] == '(':
        for l in range(lmax):
            n = 0
            for i in range(len(brac)):
                if i <= l:
                    if brac[i] == ')':
                        n += 1
                    else:
                        n -= 1
                else:
                    if brac[i] == '(':
                        n += 1
                    else:
                        n -= 1
                if n < 0:
                    break
            if n == 0:
                return True
        return False
            

    d = [None]*len(brac)
    n = 0
    for i in reversed(range(len(brac))):
        if brac[i] == ')':
            n += 1
        else:
            n -= 1
        d[i] = n



if test(input()):
    print('possible')
else:
    print('impossible')
