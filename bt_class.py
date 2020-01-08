class bt():
    def __init__(self):
        self.data = ['root']
        
    def add(self, word1, word2, side):
        sides = {'left' : 1, 'right' : 2}
        side = sides.get(side)
        i = self.index(word1)
        if (i * 2 + side) >= len(self):
            self.data.extend(['' for i in range((i * 2 + side) - len(self) + 1)])
        self[(i * 2 + side)] = word2
        
    def children(self, word1):
        i = self.index(word1)
        res = ''
        try:
            if len(self[i * 2 + 1]) > 0:
                res += self[i * 2 + 1]
            try:
                if self[i * 2 + 1] != '':
                    res += ' '
                res += self[i * 2 + 2]
            except:
                pass
        except:
            pass
        return res        
        
    def count_nodes(self, word1):
        i = self.index(word1)
        if i * 2 + 2 < len(self) and self[i * 2 + 1] != '' and self[i * 2 + 2] != '':
            return 2 + self.count_nodes(self[i * 2 + 1]) + self.count_nodes(self[i * 2 + 2])
        elif i * 2 + 1 < len(self) and self[i * 2 + 1] != '':
            return 1 + self.count_nodes(self[i * 2 + 1])
        elif i * 2 + 2 < len(self) and self[i * 2 + 2] != '':
            return 1 + self.count_nodes(self[i * 2 + 2])
        else:
            return 0        
    
    def index(self, word):
        return self.data.index(word)
    
    def __setitem__(self, i, word):
        self.data[i] = word
    
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
        print(tree.add(item[1], item[2], item[3]))
    elif item[0] == 'children':
        print(tree.children(item[1]))
    else:
        print(tree.count_nodes(item[2]))
        
        
file.close()
