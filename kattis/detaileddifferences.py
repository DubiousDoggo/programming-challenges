for _ in range(int(input())):
    a,b=input(),input()
    print(f"{a}\n{b}\n{''.join('.'if x==y else'*'for x,y in zip(a,b))}")