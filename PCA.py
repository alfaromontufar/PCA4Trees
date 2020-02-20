import matplotlib.pyplot as plt
import matplotlib.lines as lines
# https://seaborn.pydata.org/

tree = []
weights = []
levels = []
leaves =[]

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

def showtree():
    fig = plt.figure()
    fig.add_artist(lines.Line2D([0, 1], [0, 1]))
    fig.add_artist(lines.Line2D([0, 1], [1, 0]))
    plt.show()

readtree("input.txt")
showtree()

