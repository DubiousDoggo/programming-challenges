from collections import deque


class teque:
    def __init__(self):
        self._head = deque()
        self._tail = deque()

    def __len__(self):
        return len(self._head) + len(self._tail)

    def __getitem__(self, i):
        if i < len(self._head):
            return self._head[i]
        else:
            return self._tail[i-len(self._head)]

    def _balance(self):
        while len(self._head) - 1 > len(self._tail):
            self._tail.appendleft(self._head.pop())
        while len(self._head) < len(self._tail):
            self._head.append(self._tail.popleft())

    def push_back(self, x):
        self._tail.append(x)

    def push_front(self, x):
        self._head.appendleft(x)

    def push_middle(self, x):
        self._balance()
        self._head.append(x)


tq = teque()
for _ in range(int(input())):
    c, x = input().split()
    x = int(x)
    if c == "push_back":
        tq.push_back(x)
    elif c == "push_front":
        tq.push_front(x)
    elif c == "push_middle":
        tq.push_middle(x)
    elif c == "get":
        print(tq[x])
