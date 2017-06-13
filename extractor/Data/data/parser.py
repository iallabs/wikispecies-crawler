import bs4
import urllib.request
#from collections import defaultdict

glink = 'https://species.wikimedia.org'
wlink = 'https://species.wikimedia.org/wiki/'

alpha = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Taxon_strings = ['Superkingdom',
                 'Kingdom',
                 'Infrakingdom',
                 'Subkingdom',
                 'Superregnum',
                 'Subregnum',
                 'Regna',
                 'Regnum',
                 'Cladus',
                 'Clasdis',
                 'Cladi',
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

class WebLink:
    # can store information about Taxon and it link on the website
    # this solve the typical synonyms in link problem
    # see find_taxon_data return statement
    def __init__(self, title, href='-optmised ref', class_='', indice=0):
        self.title = title
        self.href = href
        self.class_ = class_
        self.indice = indice

    def __str__(self):
        return self.title

    __repr__ = __str__

###############
# DATA PARSER #

def recursive_parse_wl(weblink):
    return recursive_parse(weblink.title, weblink.href)


#############################
def recursive_parse(name, href):
    print(' - ', name)
    elements = parse_name_href(name, href, opt='subclasses')
    print('safe')
    if elements:
        if 'Species' in elements[0].class_:
            return [[n.class_ + ' : ' + n.title] for n in elements]
        return somme([[[n.class_ + ' : ' + n.title], recursive_parse(n.title, n.href)] for n in elements])
    return []
################################quit()

#################################
def quantiv_recursion(name, href, count):
    print(' - ', name)
    if count == 0:
        print('count_limits.....')
        return []
    elements = parse_name_href(name, href, opt='subclasses')
    print('safe')
    if elements:
        if 'Species' in elements[0].class_ :
            return [[n.class_ + ' : ' + n.title] for n in elements]
        return somme([[[n.class_ + ' : ' + n.title], quantiv_recursion(n.title, n.href, count-1)] for n in elements])
    return []
######################################

def parse_name(name, opt='subclasses'):
    return parse_name_href(name, '/wiki/' + name, opt=opt)

def parse_name_href(name, href, opt='subclasses'):
    if 'redlink' in href:
        return []
    url = glink + href
    subclasses_list = []
    name_found = False
    start_parsing = False
    s = soup_urlg(url)
    j = 0
    S = 0
    memory_class = ''
    if opt == 'subclasses':
        while 1:
            if name_found and subclasses_list:
                return subclasses_list
            if name_found and S == -1:
                return subclasses_list
            if j == 0:
                compt = -1
            if j > 0:
                compt = -1
            try:
                su = s.find_all('p')[j].strings
            except IndexError:
                return subclasses_list
            #print('STEP 1')
            #print(compt, ': c')
            class_ = ''
            for i in su:
                if ':' in i:
                    i = i.split(':')[0]
                #print(' Treating ')
                if i is None or i == '\n' or i == '-' or '-' in i:
                    continue
                if i == name:
                    name_found = True
                    #print('name found ', name)
                    continue
                if is_in_taxonstrings(i):
                    compt+=1
                    if memory_class:
                        if i != memory_class:
                            return subclasses_list

                if name_found and is_in_taxonstrings(i):
                    #print('name found taxon found ', i)
                    start_parsing = True
                    class_ = i
                    if not memory_class:
                        memory_class = class_
                    continue

                if name_found and start_parsing:
                    compt += 1
                    #print(i, ' ** ', compt)
                    if memory_class != class_:
                        return subclasses_list
                    try:
                        su2 = s.find_all('p')[j].find_all('a')[compt-1]
                        #print('su2' ,su2)
                    except IndexError:
                        return subclasses_list
                    try:
                        #ssprint(su2)
                        k = su2['title']
                        if '(' in su2['title'] and ' ' in su2['title']:
                            k = k[0:k.index('(')-1]
                        subclasses_list += [WebLink(k,su2['href'],class_)]
                    except KeyError:
                        continue
                elif name_found and not is_in_taxonstrings(i):
                    S = -1
            #print(name_found)
            j += 1

    if opt == 'pclass':
        # this task is easier since where not supposed to find somthing after the key name
        memory_index = 0
        name_found = False
        j = 0
        pclass = ''
        while 1:
            su = s.find_all('p')[j].strings
            memory_index +=1
            for i in su:
                memory_index += 1
                if name == i:
                    print('name', name, memory_index)
                    name_found = True
                    break
            if name_found:
                print('searching...')
                memory_index_2 = 0
                print('memory_index_2', memory_index_2)
                for i in su:
                    memory_index_2 += 1
                    print('memory_index_2', memory_index_2)
                    if memory_index_2 == memory_index - 2:
                        return i
            j += 1
        pass

    if opt == 'synonyms':
        pass

    if opt == 'vernacular':
        pass


###########

def is_in_taxonstrings(a):
    for elem in Taxon_strings:
        if elem in a:
            return True
    return False


def somme(a):
    k = []
    for i in a:
            k += i
    return k

# t=extractor('https://species.wikimedia.org/wiki/Pteridophyta', 'Pteridophyta')
# recursive

##############################################################################

def curl_p(url):
    return urllib.request.urlopen(url).read().decode('utf-8')

# Should store a Ref class containing all synonyms of taxon to use in next research

def soup_url(url):
    soup = bs4.BeautifulSoup(curl_p(url), 'html.parser')
    return soup.find('h2').next_sibling.next_sibling.contents

def soup_urlg(url):
    soup = bs4.BeautifulSoup(curl_p(url), 'html.parser')
    return soup

def soup_(url):
    soup = bs4.BeautifulSoup(curl_p(url), 'html.parser')
    return soup.find('h2')

def kappa(a):
    return a

def isfullstr(a):
    for i in a:
        if not i in alpha:
            return False
    return True

def print_wlink(a):
    for i in a:
        print(i.title, i.href, i.class_)
