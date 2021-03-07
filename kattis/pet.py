scores = [sum(int(x) for x in input().split()) for _ in range(5)]
m = max(scores)
print(scores.index(m) + 1, m)