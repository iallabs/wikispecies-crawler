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

def soup_url(url):
    return soup.find('h2').next_sibling.next_sibling.contents


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
        i = j.string
        '''
        print('--------', i)
        print('--------', taxon_found, c)
        if i == '<br/>' or j=='\n':
            print('none')
            continue
            '''
        print(' ------ TREATING LINE : ',i)
        if not taxon_found:
            if i is None:
                print('NOOONE')
            elif (name in i):
                taxon_found = True
                print('taxon found', i)
        else:
            if not i:
                print('brk')
                continue
            for tax in Taxon_strings:
                if tax in i:
                    print('found in Taxon LIST !', i)
                    c+=1
                    print(i, 'in taxon strings')
                    if c==2:
                        print('break')
                        return data
                    break
            else:
                if i == ' - ' or j== ' - ':
                    print('-')
                    continue
                print('added data', i)
                data += [i]
                
    
'''
===> https://species.wikimedia.org/wiki/Charophyta

========================================================================================================================

>>> find_taxon_data(soup.find('h2').next_sibling.next_sibling.contents, 'Charophyta')
 ------ TREATING LINE :  Superregnum: 
 ------ TREATING LINE :  Eukaryota
 ------ TREATING LINE :  None
NOOONE
 ------ TREATING LINE :  
Regnum: 
 ------ TREATING LINE :  Plantae
 ------ TREATING LINE :  None
NOOONE
 ------ TREATING LINE :  
Phylum: 
 ------ TREATING LINE :  Charophyta
taxon found Charophyta
 ------ TREATING LINE :  None
brk
 ------ TREATING LINE :  
Classes: 
found in Taxon LIST ! 
Classes: 

Classes:  in taxon strings
 ------ TREATING LINE :  Charophyceae
added data Charophyceae
 ------ TREATING LINE :   - 
-
 ------ TREATING LINE :  Chlorokybophyceae
added data Chlorokybophyceae
 ------ TREATING LINE :   - 
-
 ------ TREATING LINE :  Coleochaetophyceae
added data Coleochaetophyceae
 ------ TREATING LINE :   - 
-
 ------ TREATING LINE :  Klebsormidiophyceae
added data Klebsormidiophyceae
 ------ TREATING LINE :   - 
-
 ------ TREATING LINE :  Mesostigmatophyceae
added data Mesostigmatophyceae
 ------ TREATING LINE :   - 
-
 ------ TREATING LINE :  Zygnematophyceae
added data Zygnematophyceae
 ------ TREATING LINE :  None
brk
 ------ TREATING LINE :  
Ordines: 
found in Taxon LIST ! 
Ordines: 

Ordines:  in taxon strings
break
'''
