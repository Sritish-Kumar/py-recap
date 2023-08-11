#COLLECTION COUNTER (shoe problem)

import collections

x=int(input())
s=collections.Counter(list(map(int,input().split(' '))))

def check(ds,p):
    global s
    global price
    s[ds]-=1
    if s[ds]==0:
        s.pop(ds)
    price+=p
    return
    



n=int(input())
price=0
for i in range(n):
    rx=list(map(int,input().split()))
    if rx[0] in s.keys():
        
        check(rx[0],rx[1])
print(price)