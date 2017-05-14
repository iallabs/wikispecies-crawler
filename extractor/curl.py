import urllib.request
# https://docs.python.org/3/howto/urllib2.html

def curl(website):
    # website shoulb at the form 'http://google.com/'
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
           'Subkingdo',
           'Superregnum',
           'Regna',
           'Regnum',
           'Superphyla',
           'Phyla',
           'Phylum',
           'Subphyla',
           'Subphylum',
           'Subdivisio',
           'Class',
           'Classes',
           'Classis',
           'Subclasses',
           'Subclass',
           'Subclassis',
           'Ordo',
           'Order',
           'Ordines'
           'Subordo',
           'Suborder',
           'Familia'
           'Familiae',
           'Genera',
           'Genus',
           ]

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
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ

def extract_path_rec(name):
    try:
        # => elements
        #
        found = False
        t=-1
        name_found = False
        for line in curl(defaultlink+name):
            if found == True:
                if name in line:
                    name_found = True
                    for i in lookfor:
                        if i in line:
                            name_class = i
                    continue
                
                if line[0] in ALPHA and name_found==True:
                    clas=''
                    name =''
                    
                    for i in line.decode("utf-8"):
                        if i==' ':
                            break
                        clas+=i
                    while b'title="' in line:
                        t = line.index(b'title="')
                        for i in line.decode("utf-8")[t+7::]:
                            if i=='"':
                                break
                            name += i
                        names+=[name]
                        line=line[t+7::]
                        
                        
                    if clas in lookfor:
                        t = lookfor.index(clas)
                        t2 = lookfor.index(name_class)
                        if t - t2>=0:
                            elements = names
                            return somme([ somme([[name], extract_path_rec(name))]for name in elements])
                            

             else:
                 if istaxonavigation(line):
                     found=True

            
    except urllib.error.HTTPError:
        return []


def somme(a):
    k=[]
    for i in a:
        k+=i
    return k
        
def operationel(link):
    pass

def istaxonavigation(line):
    pass

defaultlink ='https://species.wikimedia.org/wiki/'

D = DataCollector('https://species.wikimedia.org/wiki/Eukaryota')
a= D.extract_taxonavigation_2015('https://species.wikimedia.org/wiki/Eukaryota')
for i in a:
    print(i)


    
           
