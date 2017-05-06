listspecial = ';[](),{=}'
listword = []


@staticmethod
def extract_from(file, list_word):
    with open(file) as f:
        for i in f.readlines():
            if str(i)[0] == '*':
                print (i)
            
        
