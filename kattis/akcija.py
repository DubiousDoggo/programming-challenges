
books = sorted((int(input()) for _ in range(int(input()))), reverse=True)
t = sum(b for i, b in enumerate(books) if i % 3 != 2)
print(t)
