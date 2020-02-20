tree = []
weights = []

def readtree(filename):
    global tree, weights
    f = open(filename, "r")
    for line in f:
        info = line.split(" ")
        tree.append(info[0])
        weights.append(info[1])

def printtree():
    global tree
    for node in tree:
        print(node)

readtree("input.txt")
printtree()

