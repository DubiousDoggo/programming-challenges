import math

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

for _ in range(int(input())):
    j = iter(input().split()[1:])
    poly = [vector(float(x), float(y), 0) for x,y in zip(j, j)]
    area = sum(((poly[n-1]-poly[0]) * (poly[n]-poly[0])).magnitude() for n in range(len(poly))) / 2
    print(area)
  