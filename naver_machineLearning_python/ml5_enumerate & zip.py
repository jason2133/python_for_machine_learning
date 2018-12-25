alist = ['A', 'B', 'C']
blist = ['D', 'E', 'F']

for i, (a, b) in enumerate(zip(alist, blist)):
    print (i, a, b)