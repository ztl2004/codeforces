def tToa(zero, base, number):
	ret = []
	while 1:
		digital = number/base
		number = number%base

		if digital == 0:
			ret.append(chr(number+zero-1))
			break
		else:
			ret.append(chr(digital+zero-1))

	return ret

def aTot(zero,base,number):
	length = len(number)
	ret = 0
	for i in xrange(0,length):
		ret = ret + pow(base,length-i-1)*(ord(number[i])-zero+1)

	return ret

if __name__ == "__main__":

    n = int(raw_input())
    while n>0:
        input = raw_input()
        row = ''
        column = ''
        if input[0] == 'R':
            row,column = input.split('C')
            column = int(column)
#change column into 26...
            column_list = tToa(ord('A'),26,column)
            #merge the string
            column_new = ''.join(column_list)
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
