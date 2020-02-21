import matplotlib.pyplot as plt
import matplotlib.lines as lines
# https://seaborn.pydata.org/

tree = []
weights = []
levels = []
leaves = []
PCs = []

def read_tree(filename):
    global tree, weights
    f = open(filename, "r")
    for line in f:
        info = line.split(" ")
        tree.append(int(info[0]))
        weights.append(int(info[1]))

def print_list(lista):
    for node in lista:
        print(node)

def compute_levels_leaves():
    global tree, levels, leaves

    for i in range(len(tree)):
        if tree[i] in leaves :
            leaves.remove(tree[i])
        leaves.append(i)
        
        if tree[i] == -1:
            levels.append(0)
        else:
            levels.append(levels[tree[i]]+1)

def show_tree():
    fig = plt.figure()
    fig.add_artist(lines.Line2D([0, 1], [0, 1]))
    fig.add_artist(lines.Line2D([0, 1], [1, 0]))
    plt.show()

def compute_PCs():
    global tree, leaves, weights, PCs
    
    aux_weights = list(weights)
    aux_leaves = list(leaves)
    
    for k in range(len(leaves)):
        sums = []
        for i in range(len(aux_leaves)):
            index = aux_leaves[i]
            aux_sum = 0
            while index > 0:
                aux_sum = aux_sum + aux_weights[index]
                index = tree[index]
            sums.append(aux_sum)
        
        #print_list(sums)
        
        index_k_PC = aux_leaves[sums.index(max(sums))]

        PCs.append(index_k_PC)

        index = index_k_PC
        while index > 0:
            aux_weights[index] = 0
            index = tree[index]

read_tree("input.txt")
compute_levels_leaves()
print(leaves)
compute_PCs()
print(PCs)
#print_list(levels)


