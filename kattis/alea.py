import collections


class rand:
    def __init__(self, A, C, X):
        self.A = A
        self.C = C
        self.X = X

    def roll(self):
        self.X = (self.A*self.X+self.C) % (1 << 32)
        return (self.X >> 16) % 6 + 1


class recursive:
    def __init__(self, A, C, X):
        self.random = rand(A, C, X)

    def solve(self):
        self.dice = [self.random.roll() for _ in range(5*3*11)]
        print(self.dice)


class greedy:
    def __init__(self, A, C, X):
        self.random = rand(A, C, X)
        self.scores = dict()

    def goforlowstraight(self, rolls):
        rolled = 5
        current = rolls[:rolled]
        count = collections.Counter(current)
        for _ in range(2):  # rerolls
            for i in range(len(current)):
                if count[current[i]] > 1:
                    current[i] = rolls[rolled]
                    rolled += 1
                    count = collections.Counter(current)


    def gofornum(self, play, rolls):
        minroll = 5
        rolled = 5
        current = rolls[:rolled]
        for _ in range(2):  # rerolls
            for i in range(len(current)):
                if current[i] != play:
                    current[i] = rolls[rolled]
                    rolled += 1
                    if current[i] == play:
                        minroll = rolled

        return (play*collections.Counter(current)[play], minroll, rolled)

    def best_play(self, rolls):
        for k in range(1, 7):
            if k not in self.scores:
                value, minroll, maxroll = self.gofornum(k, rolls)
                goodness = value / (k*5)
                print(k, value, goodness)

    def solve(self):
        self.dice = [self.random.roll() for _ in range(5*3*11)]
        print(self.dice)
        return self.best_play(self.dice[:5*3])


print(greedy(69069, 5, 0).solve())
