taxomony_dict = {}
synonyms = {}
integers='9876543210'

def listof(file):
    f = open(file, "r")
    return f.readlines()




def extract_taxomony(ln):
    final=[]
    kingdom=[]
    countwhiteline=0
    nextisdata = False
    for line in ln:
        if line == '\\\n':
            continue

        if line[0]=='*' and nextisdata == True:
            kingdom.append(line)

        
        if line[0]=='=' and '1' in line:
            final.append(kingdom)
            kingdom=[]
            kingdom.append(line)
            nextisdata = True
            continue
        
    return final



for i in extract_taxomony(listof('kingdom.rtf')):
    for j in i:
        print(j)
    print('------')

    
