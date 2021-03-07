
for _ in range(int(input())):
    verts = ((int(input()), int(input())) for _ in range(int(input())))
    a = 0
    for i in range(len(verts)):
        a += verts[i-1][0]*verts[i][1] - verts[i][0]*verts[i-1][1]
    a /= 2 
