# ---------------- version 1

'''l,s=list(map(int,input().split()))
r=2
t=int((l+1)/2)
for i in range(1,l+1):
    if i<(t):
        print((i*'.|.').center(s,'-'))
    elif i==(t):
        print('WELCOME'.center(s,'-'))
    elif i>(t):
        print(((i-r)*'.|.').center(s,'-'))
        r+=2'''

# ----------------- version 2

l,s=list(map(int,input().split()))
r=2
t=int((l+1)/2)
o=[i for i in range(l) if i%2==1 ]

for i in range(0,l):
    if i<(t-1):
        print((o[i]*'.|.').center(s,'-'))
    elif i==(t-1):
        print('WELCOME'.center(s,'-'))
    elif i>(t-1):
        print(((o[i-r])*'.|.').center(s,'-'))
        r+=2