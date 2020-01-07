def letter(letter, level, way):                    #проверяет есть ли такое начало уже
    global parent_index
    for j in range(len(tree[level][way])):
        if tree[level][way][j][0] == letter:
            return way, j, tree[level][way][j][4], way
    return parent_way, parent_index, None, way


def word(array):                                         #выводит ответ
    answering = []
    for answer in range(array[0][0], -1, -1):
        answering.append(tree[answer][array[0][1]][array[0][2]][0])
        array[0][1], array[0][2] = tree[answer][array[0][1]][array[0][2]][2], tree[answer][array[0][1]][array[0][2]][3]
    return ''.join([answering[i] for i in range(len(answering) - 1, -1, -1)])   


f = open('new.txt', encoding = 'utf-8')
file = f.read().split()                       #tree[порядок буквы - 1][нужная ветка с нужным началом][буква][данные]
tree = [[[['', 0, 0, 0, 0]]], [[['а', 0, 0, 0, -1]]]] #[буква, сколько раз слово, индекс путя родителя, индекс родителя, индекс массива с детьми]

for item in file:
    n = len(item)
    i = 0
    parent_index = 0
    parent_way = 0
    way = 0
    while way != None and way > -1 and i < n:           #иду пока не наткнусь на отсутствие буквы или на конец пути или на конец слова
        parent_way, parent_index, way, last_way = letter(item[i], i + 1, way)
        i += 1
    if way == None:                 #если изначально было отсутствие буквы
        tree[i][last_way].append([item[i - 1], 0, parent_way, parent_index, -1])         #добавляю букву
        parent_way, parent_index = last_way, len(tree[i][last_way]) - 1
    for k in range(i, n):                  #добавляю отстаток слова
        if k + 1 >= len(tree):                               #если такого длинного слова еще не было
            tree.append([[[item[k], 0, parent_way, parent_index, -1]]])
            tree[k][parent_way][parent_index][4] = len(tree[k + 1]) - 1
            parent_way, parent_index = 0, 0
        else:                                                #если уже было такое длинное
            tree[k + 1].append([[item[k], 0, parent_way, parent_index, -1]])
            tree[k][parent_way][parent_index][4] = len(tree[k + 1]) - 1
            parent_way, parent_index = len(tree[k + 1]) - 1, 0
    if i == n and way != None:                               #если такое слово уже было
        tree[n][parent_way][parent_index][1] += 1
    else:
        tree[n][-1][-1][1] += 1                #прибавляю слово к последней букве
    
maximum = [[0, 0, 0], 0]
for level in range(1, len(tree)):
    for way in range(len(tree[level])):
        for letter in range(len(tree[level][way])):
            if tree[level][way][letter][1] > maximum[1]:
                maximum = [[level, way, letter], tree[level][way][letter][1]]
print(word(maximum))


f.close()