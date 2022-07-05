# artScript Compiler by Mercen Lee

from re import split
from sys import argv

try:
    if argv[1].endswith('.art'):
        file = open(argv[1], encoding = 'UTF-8').read()
    else: raise Exception('Excepted .art artScript file')
except: raise Exception('Excepted input file')

def parse(var):
    temp = split(r'(["\'])(.*?[^\\])\1| |([\+\-\*\/])', var.strip())
    return [x for x in temp if x not in ['\'', '"', '', None]]

# Parsing input and output
text = file.strip().replace('\n','')
inout = text.split(';')
for i in range(0, 2):
    if parse(inout[i])[0] == 'output': output = parse(inout[i])[1]
    elif parse(inout[i])[0] == 'input': input = parse(inout[i])[1]
    else: raise Exception('Excepted input and output')

# Parsing functions
result = split(r'[\{\}]', text.split(parse(inout[1])[1])[1][1:])[:-1]
for i in range(0, len(result), 2):
    print('# ' + result[i]); ifout = 'if '; tolist = []
    for x in result[i+1].split(';')[:-1]:
        x = parse(x)
        if x[0] in ['is', 'not', 'in', 'not in']:
            ifout += '\'' + x[1] + '\' ' + x[0] + ' ' + input + ' '
        elif x[0] in ['start', 'end']:
            ifout += input + '.' + x[0] + 'swith(\'' + x[1] + '\') '
        elif x[0] in ['and', 'or']: ifout += x[0] + ' '
        elif x[0] == 'to': tolist.append(x[1])
    print(ifout.strip() + ':')
    print('    ' + output + '(random.choice(' + str(tolist) + '))\n')
