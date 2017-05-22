import bs4
import urllib.request
from pfbiology.core.ref import Ref

glink = 'https://species.wikimedia.org/'
wlink = 'https://species.wikimedia.org/wiki/'


def curl_p(url):
    return urllib.request.urlopen(url).readline().decode('utf-8')

# Should store a Ref class containing all synonyms of taxon to use in next research

def find_taxon_data(name):
    soup = bs4.BeautifulSoup(wlink+name)
    target = soup.find('h2')
    contents = [i.string for i in target.next_sibling.next_sibling.contents]
    for i in contents:
        if not name = i
            continue
    
