def add(word1, word2, side):
    sides = {'left' : 1, 'right' : 2}
    side = sides.get(side)
    i = bt.index(word1)
    if (i * 2 + side) >= len(bt):
        bt.extend(['' for i in range((i * 2 + side) - len(bt) + 1)])
    bt[(i * 2 + side)] = word2
    
    
def children(word1):
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


def count_nodes_algorithm(word1):
    i = bt.index(word1)
    if i * 2 + 2 < len(bt) and bt[i * 2 + 1] != '' and bt[i * 2 + 2] != '':
        return 2 + count_nodes_algorithm(bt[i * 2 + 1]) + count_nodes_algorithm(bt[i * 2 + 2])
    elif i * 2 + 1 < len(bt) and bt[i * 2 + 1] != '':
        return 1 + count_nodes_algorithm(bt[i * 2 + 1])
    elif i * 2 + 2 < len(bt) and bt[i * 2 + 2] != '':
        return 1 + count_nodes_algorithm(bt[i * 2 + 2])
    else:
        return 0
    
    
def count_nodes(word1):
    print(count_nodes_algorithm(word1))
    

bt = ['root']
file = open('bt.txt')
for line in file:
    #print('COMAND:', line.rstrip())
    item = line.split()
    if item[0] == 'add':
        add(item[1], item[2], item[3])
    elif item[0] == 'children':
        children(item[1])
    else:
        count_nodes(item[2])
        
        
file.close()