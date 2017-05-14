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
           'Subkingdom',
           'Superregnum',
           'Regna',
           'Regnum',
           'Divisiones',
           'Subdivisiones',
           'Superphyla',
           'Phyla',
           'Phylum',
           'Subphyla',
           'Subphylum',
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
        for line in curl(defaultlink+name):
            if found == True:
                if name in line.decode("utf-8"):
                    name_found = True
                    for i in lookfor:
                        if i in line.decode("utf-8") or i in line.decode("utf-8")[1::]:
                            name_class = i
                        else:
                            print(">>>>>> not in ",i)
                    continue
                
                if line.decode("utf-8")[0] in ALPHA and name_found==True:
                    clas=''
                    name =''
                    
                    for i in line.decode("utf-8"):
                        if i==':' or i==' ':
                            break
                        clas+=i
                    
                    while b'title="' in line:
                        t = line.index(b'title="')
                        for i in line.decode("utf-8")[t+7::]:
                            if i=='"' or i==" ":
                                break
                            name += i
                        names+=[name]
                        name=''
                        line=line[t+7::]
                    
                    
                    if clas in lookfor:
                        t = lookfor.index(clas)
                        t2 = lookfor.index(name_class)
                        if t - t2>0:
                            return somme([[[n], extract_path_rec(n)] for n in names])
                            #return somme([ somme([[(n,), extract_path_rec(n)] for n in names])
                    else:
                        print('this class isnt in lookfor', clas)

            else:
                if istaxonavigation(line):
                    found=True

            
    except urllib.error.HTTPError:
        print('error',name)
        return []

    except UnicodeEncodeError:
        return []


def somme(a):
    k=[]
    for i in a:
            k+=i
    return k


                                         

b_ = b'<h2><span class="mw-headline" id="Taxonavigation">Taxonavigation</span>'
def istaxonavigation(line):
    return (b_ in line)

defaultlink ='https://species.wikimedia.org/wiki/'


print(extract_path_rec('Plantae'))


    
           
