l,s=list(map(int,input().split()))
r=2
t=int((l+1)/2)
for i in range(1,l+1):
    if i<(t):
        print((i*'.|.').center(s,'-'))
    elif i==(t):
        print('WELCOME'.center(s,'-'))
    elif i>(t):
        print(((i-r)*'.|.').center(s,'-'))
        r+=2


    