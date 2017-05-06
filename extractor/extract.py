listspecial = ';[](),{=}'
listword = []


@staticmethod
def extract_important(file, list_word):
    with open(file) as f:
        # d = f.readlines()
        for i in f.readlines():
            if str(i)[0] == '*':
                print (i)

                
def filter(listword):
    for i in listword:
        h = []
        a = ''
        if str(i[2]) == '{':
            break
        for char in i:
            if str(char) == '*' or str(char) == '[':
                continue
            else:
                if str(char) == ']':
                    break
                a += str(char)
        print (a)
        h.append(a)
