import urllib.request
import bs4
Taxon_strings = ['Superkingdom',
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
                 'Cladus',
                 'Order',
                 'Ordines',
                 'Subordo',
                 'Suborder',
                 'Familia',
                 'Familiae',
                 'Genera',
                 'Genus',
                 'Species']

def parse1(s, soup):
    l = []
    for i in soup:
        k = i.text.split('\n')
        if len(k)==1:
            break
        for j in range(len(k)):
            if s in k[j].split(' '):
                l.append(k[j+1])
    return l

def parse2(l):
    h = []
    k = filte(l)
    print(k)
    for i in k:
        print (i)
        if ':' in i:
            i.split(':')[-1]
            a = urllib.request.urlopen("https://species.wikimedia.org/wiki/" + i)
            soup = bs4.BeautifulSoup(a.read(), 'html.parser')
            soup = soup.find_all('p')
            h.append(parse1(i), soup)
        a = urllib.request.urlopen("https://species.wikimedia.org/wiki/" + i)
        soup = bs4.BeautifulSoup(a.read(), 'html.parser')
        soup = soup.find_all('p')
        h.append(parse1(i, soup))
    return h
'''
def filte(l):
    k = l[0].split(':')
    print(k)
    if isinlist(k[0], Taxon_strings):
        for  i in k[1].split('-'):
            #if '(':
'''
def isinlist(s, Taxon_strings):
    if ' ' in s:
        if s.split(' ')[0] in Taxon_strings:
            return True
    return False
'''
a = urllib.request.urlopen("https://species.wikimedia.org/wiki/Plantae ")
soup = bs4.BeautifulSoup(a.read(), 'html.parser')
soup = soup.find_all('p')
s = "Plantae"
print(parse2(parse1(s, soup)))
'''
