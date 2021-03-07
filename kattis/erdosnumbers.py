from sys import stdin

collab = {'PAUL_ERDOS': []}
authors = []
for line in stdin:
    a, *b = line.split()
    authors.append(a)
    collab.setdefault(a, []).extend(b)
    for c in b:
        collab.setdefault(c, []).append(a)

number = {'PAUL_ERDOS': 0}
queue = ['PAUL_ERDOS']
while len(queue):
    a = queue.pop()
    for c in collab[a]:
        if c not in number or number[c] > number[a] + 1:
            number[c] = number[a] + 1
            queue.append(c)

for a in authors:
    print(a, number.setdefault(a, 'no-connection'))
