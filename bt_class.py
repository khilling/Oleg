import sys


def add(bt, word1, word2, side):
    sides = {'left' : 1, 'right' : 2}
    side = sides.get(side)
    i = bt.index(word1)
    if (i * 2 + side) >= len(bt):
        bt.extend(['' for i in range((i * 2 + side) - len(bt) + 1)])
    bt[(i * 2 + side)] = word2


def children(bt, word1):
    i = bt.index(word1)
    try:
        if len(bt[i * 2 + 1]) > 0:
            print(bt[i * 2 + 1], end = ' ')
        try:
            print(bt[i * 2 + 2])
        except:
            pass
    except:
        print('')


def count_nodes_algorithm(bt, word1):
    i = bt.index(word1)
    if i * 2 + 2 < len(bt) and bt[i * 2 + 1] != '' and bt[i * 2 + 2] != '':
        return 2 + count_nodes_algorithm(bt, bt[i * 2 + 1]) + count_nodes_algorithm(bt, bt[i * 2 + 2])
    elif i * 2 + 1 < len(bt) and bt[i * 2 + 1] != '':
        return 1 + count_nodes_algorithm(bt, bt[i * 2 + 1])
    elif i * 2 + 2 < len(bt) and bt[i * 2 + 2] != '':
        return 1 + count_nodes_algorithm(bt, bt[i * 2 + 2])
    else:
        return 0
    
    
def count_nodes(bt, word1):
    print(count_nodes_algorithm(bt, word1))


class bt():
    def __init__(self):
        self.data = ['root']
        
    def add(self, word1, word2, side):
        add(self.data, word1, word2, side)
        
    def children(self, word1):
        children(self, word1)
        
    def count_nodes(self, word1):
        count_nodes(self, word1)
    
    def index(self, word):
        return self.data.index(word)
    
    def __repr__(self):
        return str(self.data)
        
    def __getitem__(self, i):
        return self.data[i]
    
    
    def __len__(self):
        return len(self.data)


file = open('bt.txt')
tree = bt()
for line in file:
    print('COMAND:', line.rstrip())
    print('TREE:', tree)
    item = line.split()
    if item[0] == 'add':
        tree.add(item[1], item[2], item[3])
    elif item[0] == 'children':
        tree.children(item[1])
    else:
        tree.count_nodes(item[2])
        
        
file.close()