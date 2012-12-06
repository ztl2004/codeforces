n = input()

sum = {}
b = []

for x in range(n):
    name,value = raw_input().split(' ')
    if sum.has_key(name):
        sum[name] += int(value)
    else:
        sum[name] = int(value)
    b.append((name,sum[name]))
        
max = max(sum.values()) 

for name,value in b:
    if value >= max and sum[name] == max:
        print name
        break