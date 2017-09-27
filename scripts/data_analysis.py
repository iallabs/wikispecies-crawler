listspecial = ';[](),{=}'
listword = []
list_class = ['Empire', 'Superkingdom','Kingdom' ,'Subkingdom', 'Infrakingdom',
              'Grade','Superphylum', 'Phylum','Subphylum','Dominion', 
              'Subdominion', 'Superclass', 'Class', 'Subclass', 'Order', 'group']



def extract_important(file, list_word):
    with open(file) as f:
        # d = f.readlines()
        for i in f.readlines():
            if str(i)[0] == '*':
                print (i)

                
def filter1(listword):
    v = []
    a = []
    s = 0
    for s in range(len(listword)-1):
        if listword[s][2] == '{':
            break
        if listword[s].count('*') < listword[s+1].count('*'):
            while listword[s].count('*') < listword[s+1].count('*'):
                a.append(listword[s])
                s += 1
            while listword[s].count('*') == listword[s+1].count('*'):
                a.append(listword[s])
                s +=1
            v.append(a)
        else:
            v.append(listword[s])
            a = []
def get_etoile(lista):
    a = []
    for i in range(len(lista)):
        a.append(lista[i].count('*'))
    return a
  
def remove_car(mot):
    a = mot.split('*')
    j = 0
    while a.count('')!= 0:
       a = a.remove('')
       j += 1
    return a, j
  
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
