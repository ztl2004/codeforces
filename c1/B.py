import re

n = input() 
for x in range(n):
    input = raw_input()
    p = re.match(r'R(\d+)C(\d+)',input)

    base = 26
    zero = ord('A')

    if p: 
        row = p.group(1)
        column = int(p.group(2))
        #change column into 26...
        while column:
            digital = (column-1)%base
            row = chr(digital+zero) + row
            column = (column-1)/base
    else:
        p = re.match(r'(\D+)(\d+)',input)
        row = 'R' + p.group(2) + 'C' 

        #change column into 10
        ret = 0
        for x in p.group(1): 
            ret = ret*base + ord(x)-zero+1
        row += str(ret)
    print row