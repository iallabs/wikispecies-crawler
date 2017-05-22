import bs4
import urllib.request
from pfbiology.core.ref import Ref

glink = 'https://species.wikimedia.org/'
wlink = 'https://species.wikimedia.org/wiki/'


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
    for j in contents:
        i = j.string
        print(i)
        if not taxon_found:
            if not (name == i):
                continue
            else:
                taxon_found = True
        else:
            if i in Taxon_Strings:
                return data
            else:
                if i==' - ':
                    continue
                data+=[i]
                
    
