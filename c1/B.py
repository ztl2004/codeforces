n = input() 
for x in range(n):
    input = raw_input()
    row = ''
    column = ''
    base = 26
    zero = ord('A')

    if input[0] == 'R':
        row,column = input.split('C')
        column = int(column)
        ret = ''
        #change column into 26...
        while column:
            digital = (column-1)%base
            ret = chr(digital+zero) + ret
            column = (column-1)/base
        print ret+row[1:]
    else:
        for i in xrange(0,len(input)):
            if input[i] < 'A':
                row = input[i:]
                column = input[:i]
                break

        #change column into 10
        ret = 0
        for x in column: 
            ret = ret*base + ord(x)-zero+1
        print 'R'+row+'C'+str(ret) 
