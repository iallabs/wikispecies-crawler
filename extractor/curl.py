import urllib.request
# https://docs.python.org/3/howto/urllib2.html
import pickle

def curl(website):
    # website shoulb at the form 'http://google.com'
    R = urllib.request.urlopen(website)
    for i in R:
        print(i)



# values = dict()
def request(website, values):
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(website, data)
    R = urllib.request.urlopen(req)
    return R.readlines()
    
    
lookfor = ['Superkingdom',
           'Kingdom',
           'Infrakingdom',
           'Subkingdom',
           'Superregnum',
           'Regna',
           'Regnum',
           'Superphyla',
           'Phyla',
           'Phylum',
           'Subphyla',
           'Subphylum',
           'Divisio',
           'Divisiones',
           'Subdivisiones',
           'Subdivisio',
           'Classis',
           'Class',
           'Classes',
           'Subclassis',
           'Subclasses',
           'Subclass',
           'Ordo',
           'Order',
           'Ordines',
           'Subordo',
           'Suborder',
           'Familia',
           'Familiae',
           'Genera',
           'Genus',
           'Species']

ul_ = b'</ul>'
li_ = b'</li>'
ul = b'<ul>'
li = b'<li>'
title = 'tilte'
href = 'href'
div = '<div '
taxonavigation = ['Taxon Navigation', 'Taxonavigation']

import urllib.request


class DataCollector(object):

    def __init__(self, website):
        self.website = website
        self.taxonavigation = []
        self.taxon_history = [[]]

    def curl(self, website):
        return urllib.request.urlopen(website)
        
    def extract_taxon_history(self, link):
        pass

    def extract_taxonavigation_2015(self, link):
        found = False
        taxonomy = []
        etoile = ''
        name_found = False
        for line in self.curl(link):
            if found == False and not istaxonavigation(line):
                continue
            else:
                found = True
                if line[0:3] == b'<h3' and name_found == True:
                    return taxonomy

                count = True
                if line[0:4] == b'<ul>':
                    etoile += '*'
                    continue
                if line[0:5] == li_:
                    etoile = etoile[1::]
                    continue
                if line[0:4] == li:
                    clas=''
                    name =''
                    
                    for i in line[4::].decode("utf-8"):
                        if i==' ':
                            break
                        clas+=i
                    if b'wiki/' in line:
                        t = line.index(b'wiki/')
                    
                        for i in line.decode("utf-8")[t+5::]:
                            if i=='"':
                                break
                            name += i
                        
                    taxonomy+=[(etoile, clas, name)]
        return taxonomy
                

def curl(website):
        return urllib.request.urlopen(website)                


alpha = 'abcdefghijklmnopqrstuvwxyz'
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def extract_path_rec(name):
    
    try:
        # => elements
        #
        found = False
        t=-1
        name_found = False
        names=[]
        name_class=''
        specie_found=False
        for line in curl(defaultlink+name):
            
            if specie_found:
                if line.decode("utf-8")[0] in ALPHA:
                    clas=''
                    name =''
                    
                    for i in line.decode("utf-8"):
                        if i==':' or i==' ':
                            break
                        clas+=i
                        
                    while b'" title="' in line:
                        t = line.decode("utf-8").index('" title="')
                        for i in line.decode("utf-8")[t+9::]:
                            if i == ' ':
                                i='_'
                            if i == '(' or i=='"':
                                break
                            name+=i
                        names+=[name[:len(name)-1]]
                        name=''
                        line=line[t+8::]
                    print(clas, '-->' ,names)
                    return names
        
            if found == True:

                if name in line.decode("utf-8") and not specie_found:
                    name_found = True
                    for i in lookfor:
                        if i in line.decode("utf-8"):
                            name_class = i
                            #print(line, 'ENDHERE', 'CLASS',name_class)
                            if name_class == 'Genus':
                                specie_found = True
                    
                    continue
            
                if line.decode("utf-8")[0]=='<':
                    continue
                if line.decode("utf-8")[0] in ALPHA and name_found==True:
                    clas=''
                    name =''
                    
                    for i in line.decode("utf-8"):
                        if i==':' or i==' ':
                            break
                        clas+=i
                    
                    while b'title="' in line:
                        t = line.decode("utf-8").index('title="')
                        for i in line.decode("utf-8")[t+7::]:
                            if clas != 'Species' and (i == '"' or i == " "):
                                break
                            elif clas == 'Species':
                                print('SPCIIIES')
                                if i == ' ':
                                    i='_'
                                if i == '"':
                                    break
                            name+=i
                        
                        names+=[name]
                        name=''
                        line=line[t+6::]
                    
                    print(clas, ' > ', names)
                    if clas in lookfor:
                        t = lookfor.index(clas)
                        t2 = lookfor.index(name_class)
                        if t == len(lookfor) - 1:
                            return [[name] for name in names]
                        if t - t2>0:
                            return somme([[[clas + ' : ' + n], extract_path_rec(n)] for n in names])
                            #return somme([ somme([[(n,), extract_path_rec(n)] for n in names])

            else:
                if istaxonavigation(line):
                    found=True

            
    except urllib.error.HTTPError:
        return []

    except UnicodeEncodeError:
        return []

    except ValueError:
        return []


def somme(a):
    k=[]
    for i in a:
            k+=i
    return k

def etoile(n):
    a=''
    for i in range(n):
        a+='*'
    return a
                                         
def read_matrix(obj,level):
    if type(obj)==type([]):
        if len(obj)>1:
            for i in obj:
                read_matrix(i,level+1)
        if len(obj)==1:
            read_matrix(obj[0], level)
        
    else:
        if type(obj) ==type('rer'):
            print(etoile(level) + "  " +obj)




b_ = b'<h2><span class="mw-headline" id="Taxonavigation">Taxonavigation</span>'
def istaxonavigation(line):
    return (b_ in line)

defaultlink ='https://species.wikimedia.org/wiki/'

# /!\ Unremark this if its the first time runing
a=extract_path_rec('Plantae')
pickle.dump(a, open("data.saved", "wb"))

# use this after data is saved with pickle
#a=pickle.load(open("data.saved", "rb"))

for i in a:
    print(i)
print('--')
read_matrix(a,0)
