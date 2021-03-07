
def quadrant(x: int, y: int):
    if y >= 0 and x > 0:
        return 1
    if y > 0 and x <= 0:
        return 2
    if y <= 0 and x < 0:
        return 3
    if y < 0 and x >= 0:
        return 4


while True:
    p = []
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        p.append([int(x) for x in input().split()])
    for _ in range(int(input())):
        x, y = (int(i) for i in input().split())
        pt = [[px - x, py - y] for px, py in p]
        a = 0
        # janky hack
        for i in range(len(pt)):
            x1, y1 = pt[i-1]
            x2, y2 = pt[i]
            q1 = quadrant(x1, y1)
            q2 = quadrant(x2, y2)
            if q1 == None or q2 == None:
                print("on")
                break
            if q1 != q2:
                if q1 == 1:
                    if q2 == 2:
                        a += 1
                    elif q2 == 3:
                        s1 = abs(x1/y1)
                        s2 = abs(x2/y2)
                        if s1 == s2:
                            print("on")
                            break
                        if s2 > s1:
                            a += 2
                        else:
                            a -= 2
                    elif q2 == 4:
                        a -= 1
                elif q1 == 2:
                    if q2 == 1:
                        a -= 1
                    elif q2 == 3:
                        a += 1
                    elif q2 == 4:
                        s1 = abs(y1/x1)
                        s2 = abs(y2/x2)
                        if s1 == s2:
                            print("on")
                            break
                        if s2 > s1:
                            a += 2
                        else:
                            a -= 2
                elif q1 == 3:
                    if q2 == 1:
                        s1 = abs(x1/y1)
                        s2 = abs(x2/y2)
                        if s1 == s2:
                            print("on")
                            break
                        if s2 > s1:
                            a += 2
                        else:
                            a -= 2
                    elif q2 == 2:
                        a -= 1
                    elif q2 == 4:
                        a += 1
                elif q1 == 4:
                    if q2 == 1:
                        a += 1
                    elif q2 == 2:
                        s1 = abs(x1/y1)
                        s2 = abs(x2/y2)
                        if s1 == s2:
                            print("on")
                            break
                        if s2 < s1:
                            a += 2
                        else:
                            a -= 2
                    elif q2 == 3:
                        a -= 1
        else:
            if a != 0:
                print("in")
            else:
                print("out")
