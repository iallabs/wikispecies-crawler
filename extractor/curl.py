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
           'Regnum',
           'Superphyla',
           'Phyla']

ul_ = b'</ul>'
li_ = b'</li>'
ul = b'<ul>'
li = b'<li>'
title = 'tilte'
href = 'href'
div = '<div '
taxonavigation = ['Taxon Navigation', 'Taxonavigation']



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
        count = False
        for line in self.curl(link):
            if found == False and line != b'<h3><span class="mw-headline" id="Ruggiero_et_al._.282015.29">Ruggiero et al. (2015)</span></h3>\n':
                
                continue
            else:
                found = True
                if line[0:3] == b'<h3' and count == True:
                    
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
                
                

    def extract_path_rec(self, link, sample):
        pass



D = DataCollector('https://species.wikimedia.org/wiki/Eukaryota')
a= D.extract_taxonavigation_2015('https://species.wikimedia.org/wiki/Eukaryota')
for i in a:
    print(i)

    
           
