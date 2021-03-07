import math
import itertools


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, rhs):
        return vector(self.x + rhs.x, self.y + rhs.y, self.z + rhs.z)

    def __sub__(self, rhs):
        return vector(self.x - rhs.x, self.y - rhs.y, self.z - rhs.z)

    def __matmul__(self, rhs):
        return self.x * rhs.x + self.y * rhs.y + self.z * rhs.z

    def __mul__(self, rhs):
        return vector(
            self.y * rhs.z - self.z * rhs.y,
            self.z * rhs.x - self.x * rhs.z,
            self.x * rhs.y - self.y * rhs.x,
        )

    def __neg__(self):
        return vector(-self.x, -self.y, -self.z)

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y and self.z == rhs.z

    def magnitude(self):
        return math.sqrt(self @ self)

    def unit(self):
        mag = self.magnitude()
        return vector(self.x / mag, self.y / mag, self.z / mag)


total = 0
n = int(input())
for _ in range(n):
    f = int(input())
    faces = [None] * f
    for i in range(f):
        j = iter(input().split()[1:])
        faces[i] = [vector(float(x), float(y), float(z)) for x, y, z in zip(j, j, j)]

    # propagate the orientation of each face
    orientation = [None] * f
    orientation[0] = 1
    queue = [0]
    while len(queue):
        q = queue.pop(0)
        fq = faces[q]
        for i, fi in enumerate(faces):
            if orientation[i] == None:
                for j, k in itertools.product(range(len(fi)), range(len(fq))):
                    if fi[j] == fq[k-1] and fi[j-1] == fq[k]:
                        orientation[i] = orientation[q]
                        queue.append(i)
                        break
                    if fi[j] == fq[k] and fi[j-1] == fq[k-1]:
                        orientation[i] = -orientation[q]
                        queue.append(i)
                        break

    # calculate volume using divergence theorem
    # https://en.wikipedia.org/wiki/Polyhedron#Volume
    volume = 0
    for i, fi in enumerate(faces):
        norm = ((fi[1] - fi[0]) * (fi[2] - fi[0])).unit()
        # calculate area of face using cross-product parallelogram method
        area = sum(((fi[n-1]-fi[0]) * (fi[n]-fi[0])).magnitude() for n in range(len(fi))) / 2
        volume += orientation[i] * (fi[0] @ norm) * area
    total += abs(volume / 3)

print(f'{total:.2f}')
