def tToa(zero, base, number):
	ret = '' 
	while number:
		digital = (number-1)%base
		ret = chr(digital+zero) + ret
		number = (number-1)/base
	return ret

def aTot(zero,base,number):
	ret = 0
	for x in number: 
		ret = ret*base + ord(x)-zero+1

	return ret

if __name__ == "__main__":

    n = input() 
    for x in range(n):
        input = raw_input()
        row = ''
        column = ''
        if input[0] == 'R':
            row,column = input.split('C')
            column = int(column)
            #change column into 26...
            column_new = tToa(ord('A'),26,column)
            print column_new+row[1:]
        else:
            for i in xrange(0,len(input)):
                if input[i] < 'A':
                    row = input[i:]
                    column = input[:i]
                    break

            #change column into 10
            column = aTot(ord('A'),26,column)
            print 'R'+row+'C'+str(column)
