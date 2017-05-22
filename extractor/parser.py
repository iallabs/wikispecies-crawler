import bs4
import urllib.request
from pfbiology.core.ref import Ref

glink = 'https://species.wikimedia.org/'
wlink = 'https://species.wikimedia.org/wiki/'

Taxon_strings = ['SuperKingdom'
                 'Kingdom',
                 'SubKingdom',
                 'InfraKingdom',
                 'Regnum',
                 'SubRegnum',
                 'Phylum',
                 'SubPhylum',
                 'Class',
                 'SubClass',
                 'Order',
                 'SubOrder',
                 'Familly',
                 'SubFamilly',
                 'Tribe',
                 'SubTribe',
                 'Genus',
                 'SubGenus',
                 'Section',
                 'SubSection',
                 'Series',
                 'SubSeries',
                 'Species',
                 'SubSpecies',
                 'Variety',
                 'Divisiones',
                 'Subdivisiones',
                 'Ordines',
                 'Familia',
                 'Ordo',
                 'Familiae',
                 'Genera',
                 'Classis',
                 'Classes',
                 'Subclasses',
                 'Subclassis']

def curl_p(url):
    return urllib.request.urlopen(url).readline().decode('utf-8')

# Should store a Ref class containing all synonyms of taxon to use in next research

find_taxon_data(soup.find('h2').next_sibling.next_sibling.contents, 'Charophyta')

def find_taxon_data(contents, name):
    '''
    soup = bs4.BeautifulSoup(wlink+name)
    target = soup.find('h2')
    contents = [i.string for i in target.next_sibling.next_sibling.contents]
    '''
    taxon_found = False
    nefew_taxon = False
    data = []
    c=0
    for j in contents:
        print('--------', j)
        print('--------', taxon_found, c)
        i = j.string
        if i == '<br/>' or j=='\n':
            print('none')
            continue
        if not taxon_found:
            if i is None:
                print('noooooonnnnneeeee')
            elif not (name == i[0:len(i)-1]):
                print('not name', i)
                continue
            else:
                taxon_found = True
                print('taxon found', i)
        else:
            if not i:
                print('brk')
                continue
            if i[0:len(i)-1] in Taxon_strings:
                c+=1
                print(i, 'in taxon strings')
                if c==2:
                    print('break')
                    return data
            else:
                if i==' - ' or j==' - ':
                    print('-')
                    continue
                print('added data', i)
                data+=[i]
                
    
