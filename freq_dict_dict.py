def freq(text):
    freq_dict = {}
    for item in text:
        try:
            freq_dict[item] += 1
        except KeyError:
            freq_dict[item] = 1
    return freq_dict


file = open('pushkin.txt', encoding = 'utf-8')
text_pushkin = [i.lower() for i in file.read().split()]
file.close()
new_text = []
literature = ['mumu.txt', 'lermontov.txt', 'anna.txt', 'poemes1.txt', 'poemes2.txt']
for item in literature:
    file2 = open(item, encoding = 'utf-8')
    text2 = [i.lower() for i in file2.read().split()]
    file2.close()
    new_text += text2
freq_dict = sorted(list(freq(text_pushkin).items()), key = lambda tuple: tuple[1], reverse = True)
freq_dict2_values = [i[0] for i in sorted(list(freq(new_text).items()), key = lambda tuple: tuple[1], reverse = True)[:100]]
n = int(input()) #n most freq words
flag = 0
i = 0
while flag < n:
    if freq_dict[i][0] not in freq_dict2_values:
        print(freq_dict[i], end = ' ')
        flag += 1
    i += 1
    
    