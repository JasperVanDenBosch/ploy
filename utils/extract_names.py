firstnames = set()
lastnames = set()
with open('names.txt','r') as fnames:
    for line in fnames.readlines():
        if len(line) < 3:
            continue
        parts1 = line.split(',')
        parts = parts1[0].split()
        firstname = parts[0]
        firstnames.add(firstname)
        if len(parts) > 1:
            lastnames.add(' '.join(parts[1:]))

#with open('firstnames.txt','w') as ffirstnames:
#    with open('lastnames.txt','w') as flastnames:
with open('firstnames.txt','w') as ffirstnames:
    for name in firstnames:
        ffirstnames.write(name+'\n')

with open('lastnames.txt','w') as flastnames:
    for name in lastnames:
        flastnames.write(name+'\n')
