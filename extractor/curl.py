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

ul_ = '</ul>'
li_ = '</li>'
ul = '<ul>'
li = '</li>'
title = 'tilte'
href = 'href'
div = '<div '
taxonavigation = ['Taxon Navigation', 'Taxonavigation']

class DataCollector(object):

    def __init__(self, website):
        self.website = website
        self.taxonavigation = []
        self.taxon_history = [[]]

    def curl(self):
        pass

    def extract_taxon_history(self, link):
        pass

    def extract_taxonavigation(self):
        pass

    def extract_path_rec(self, link, order_rules):
        pass

    
           
