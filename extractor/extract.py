listspecial = ';[](),{=}'
listword = []


@staticmethod
def extract_important(file, list_word):
    with open(file) as f:
        # d = f.readlines()
        for i in f.readlines():
            if str(i)[0] == '*':
                print (i)
            
        
