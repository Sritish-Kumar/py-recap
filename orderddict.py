#This code too is written in one shot. It can be reducued to a shorter and more efficient version. 
# You can try it on your own. 

import collections
n=int(input())

od=collections.OrderedDict()

def st(s):
    name=''
    price=0
    for i in range(len(s)-1,-1,-1):
        if s[i].isdigit()==True:
            price+=int(s[i])
            s.pop(i)
            name+=' '.join(s)
    return name,price        


for i in range(n):
    s=input().split()
    name,price=st(s)
    if name in od:
        od[name]+=int(price)
    else:
        od[name]=price
for i in od:
    print(i, od[i])