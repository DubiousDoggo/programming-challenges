rm,cm = [int(x) for x in input().split()]

a = [[*input()] for _ in range(rm)]

for _ in range(int(input())):
	
	r1,c1,r2,c2 = [int(x)-1 for x in input().split()]
	if r1 > r2:
		r1,r2 = r2,r1
		c1,c2 = c2,c1

	if a[r1][c1] != a[r2][c2]:
		print('neither')
	else:
		v = a[r1][c1]
		tmp = a[r1]

		cont = True
		for i in range(c1,cm):
			if cont:
				if tmp[i] != v:
					cont = False
			else:
				tmp[i] = 'x'
		
		cont = True
		for i in range(c1,-1,-1):
			if cont:
				if tmp[i] != v:
					cont = False
			else:
				tmp[i] = 'x'
	
	
		print(tmp)


