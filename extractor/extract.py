listspecial = ';[](),{=}'
listword = []



def extract_from(file, list_word):
    with open(file, 'r', encoding = 'utf-8', errors= 'ignore') as f:
        for lines in f.read():
            if len(lines) == 0 or str(lines)[0] != '*':
                continue
            word = ''
            for i in lines:
                if str(i) in list_special:
                    continue
                    while (not str(i) in list_special):
                        word += str(i)
                        print (word)
                        list_word.append(word)
