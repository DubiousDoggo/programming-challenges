
A0Long = 2**(1/4)
sqrt2 = 2**(1/2)


def longEnd(size):
    if size % 2:
        return sqrt2 * (A0Long / (2**((size+1)/2)))
    else:
        return A0Long / (2**(size/2))


endCache = [longEnd(x) for x in range(40)]


def make(size, count, papers):
    if size >= len(papers):
        raise StopIteration

    if count <= papers[size]:
        papers[size] -= count
        return 0
    else:
        if size+1 >= len(papers):
            raise StopIteration
        count -= papers[size]
        papers[size] = 0
        return longEnd(size+1)*count + make(size+1, count*2, papers)


input()
papers = [0, 0]+[int(x) for x in input().split(' ')]

try:
    print(make(1, 1, papers))
except StopIteration:
    print('impossible')
