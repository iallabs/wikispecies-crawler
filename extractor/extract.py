listspecial = ';[](),{=}'
listword = []



def extract_important(file, list_word):
    with open(file) as f:
        # d = f.readlines()
        for i in f.readlines():
            if str(i)[0] == '*':
                print (i)

                
def filter1(listword):
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
        
def filter2(h):
    k = []
    l = []
    for i in range(len(h)-1):
        a = h[i].split(' ')
        if len(a) == 0:
            continue
        elif len(a) > 1:
            if a[0] in list_class:
                k.append(a)
            elif (len(a) == 2 and a[1] not in list_class):
            l.append(a[1])
        else:
            l.append(a)
print(k)
#
#
#
print(l)   
