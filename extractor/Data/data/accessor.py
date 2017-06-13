import os
this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "plantae.txt")
data = [i for i in open(DATA_PATH).readlines()]
data_test_1 = []
data_test_2 = []
data_test_cyclic = []
data_test_nonordered = []

from .parser import WebLink

d = {'Divisiones' : 'Phylum',
     'Subdivisiones' : 'SubPhylum',
     'Ordines' : 'Order',
     'Familia' : 'Familly',
     'Ordo' : 'Order',
     'Phyla' : 'Phylum',
     'Subregnum' : 'SubRegnum',
     'Cladi' : 'Phylum',
     'Cladus' : 'Phylum2',
     'Familiae' : 'Familly',
     'Genera' : 'Genus',
     'Classis' : 'Class',
     'Classes' : 'Class',
     'Subclasses' : 'SubClass',
     'Subclassis' : 'SubClass',
     'enera' : 'Genus',
     'pecies' : 'Species',
     'amiliae' : 'Familly',
     'amilia' : 'Familly',
     'ubphyla' : 'SubPhylum',
     'lassis' : 'Class',
     'rdo' : 'Order',
     'enus' : 'Genus',
     'rdines' : 'Order',
     'lasses' : 'Class',
     'ubclasses' : 'SubClass'}

########################################
# from recursive_parse to linearised data
# weblink => tuple

# Use prepare_1 after importing data from wikispecies using:
# parse_name , parse_name_href, recursive_parse
def prepare_1(ln):
    return optimise_data(dematrixit(ln))

def prepare_2(ln):
    return optimise_data_2(dematrixit(ln))

# example :
# a = recursive_parse('Charophyta', '/wiki/Charophyta')
# head =  Contructor(prepare_1(a)).head
# do not use without verification with all .txt data

def change_d(t):
    if t in d.keys():
        return d[t]
    return t


# OPTIMISATION FROM LIST OF TYPE STR LIST
# TO TYPLE LIST
def optimise_data(data):
    lp = []
    for i in data:
        a, b = i.split(':')
        t = a.split(' ')
        lp += [(t[0], change_d(t[2]), b[1:-1:])]
    return lp

def optimise_data_2(data):
    lp = []
    for i in data:
        a, b = i.split(':')
        t = a.split(' ')
        lp += [(t[0], change_d(t[1]), b[1:])]
    return lp

# Transform the first out put from parser function
# into a STR LIST
def dematrixit(obj):
    base = []
    def dematrix(obj, level, base):
        if type(obj)==type([]):
            if len(obj)>1:
                for i in obj:
                    dematrix(i,level+1, base)
            if len(obj)==1:
                dematrix(obj[0], level, base)
        else:
            if obj.__class__ == WebLink:
                base += [etoile(level) + ' '+ obj.class_[1::] +' : ' + obj.title]
            if type(obj) == str:
                base += [etoile(level) + ' '+ obj.split(' : ')[0][1::] + ' : ' + obj.split(' : ')[1]]
    dematrix(obj, 0, base)
    return base

def etoile(n):
    return n * '*'

def correct_data(data):
    lp = []
    for i in data:
        k = i.split(' ')
        if len(k)==3:
            lp += [(k[0], 'Species', k[2])]
        else:
            lp += [(k[0], change_d(k[2]), k[4])]
    return lp

def open_data(name):
    with open(name + '.txt', "r") as file:
        ln = []
        for i in file.readlines():
            ln.append(i)
        return ln
