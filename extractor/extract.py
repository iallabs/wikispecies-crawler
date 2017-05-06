class extract():
    def __init__(self):
        self.wordlist = []
        self.listspecial = ';[](),={}'
        
        def extract_from(file):
            with open(file, 'r', encoding = 'utf-8', errors= 'ignore') as f:
                for lines in f:
                    if len(lines) == 0:
                        continue
                    for i in lines:
                        if str(i) != '*':
                            
                        else:
                            word = ''
                            if str(i) in list_special:
                                continue
                            while str(i) not in list_special:
                                word += str(i)
                            print (word)
                            list_word.append(word)
