l=[('*', 'Kingdom', 'Plantae'),
   ('**', 'Phylum', 'Algae'),
   ('**', 'Phylum', 'Bryophyta'),
   ('***', 'SubPhylum', 'Bryopsida'),
   ('**', 'Phylum', 'Cracophyta'),
   ('**', 'Phylum', 'Cinqophyta'),
   ('***', 'Order', 'Pitana')]

import pickle

d = {'Divisiones' : 'Phylum',
     'Subdivisiones' : 'SubPhylum',
     'Ordines' : 'Order',
     'Familia' : 'Familly',
     'Ordo' : 'Order',
     'Familiae' : 'Familly',
     'Genera' : 'Genus',
     'Classis' : 'Class',
     'Classes' : 'Class',
     'Subclasses' : 'SubClass',
     'Subclassis' : 'SubClass'}
     
lk=[]
#a=pickle.load(open("data.saved", "rb"))

data = open('plantae.txt', 'r')

def transf_ligne(line):
    global d
    l = line.split(' ')
    if '_' in line:
        return (l[0], 'species', 'nan')
    if l[2] in list(d.keys()):
        return (l[0], d[l[2]], l[4][:len(l[4])-1])
    return (l[0], l[2], l[4][:len(l[4])-1])



for i in data.readlines():
    lk+=[transf_ligne(i)]


#for i in range(0, len(lk)):
    #print(lk[i])
        

def trans(fil):
    ln=[]
    for i in fil:
        ln+=[transf_ligne(i)]
    return ln

ln = []

def etoile(n):
    a=''
    for i in range(n):
        a+='*'
    return a
                                         

def write_matrix(obj, level):
    global ln
    if type(obj)==type([]):
        if len(obj)>1:
            for i in obj:
                write_matrix(i,level+1)
        if len(obj)==1:
            write_matrix(obj[0], level)
        
    else:
        if type(obj) ==type('rer'):
            ln+=[etoile(level) + "  " +obj]
            
from pfbiology.factory.constructor import Constructor

#c=Constructor(trans(a))
#write_matrix(lk, 0)
#print(list(d.keys()))
#mn = trans(ln)
'''
for i in trans(ln):
    print(i)
    '''
#ln=trans(ln)
c=Constructor(lk)
#for i in trans(ln):
#    print(i)
#print(c.head.branches)
print(c.head)
print(c.head.subclasses)
for i in c.head.subclasses:
    print(i.subclasses)
#print(c._args)
for i in c.head.subclasses[1].subclasses:
    print(i, i.calculate_cousins())
