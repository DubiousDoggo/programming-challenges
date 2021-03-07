class part:
    def __init__(self, desc, cur, min, max):
        self.desc = desc
        self.cur = int(cur)
        self.min = int(min)
        self.max = int(max)


def setup(inventory):
    with open('inventory.csv') as infile:
        for row in infile:
            inventory.append(part(*row.split(',')))
