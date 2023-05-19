d='abcdefghijklmnopqrstuvwxyz'
n=int(input())


bit=4*n-3   #length
t=2*n-1  #breadth
od=[i for i in range(1,2*n,2)] #odd numbers

print(od)
for i in range(0,t):
    if i<(t-1)/2:
        print('top')
        for j in range(od[i]):
            print('times:',j)



    elif i==(t-1)/2:
        print('middle')
    elif i>(t-1)/2:
        print('bottom')
        

            


print('bit:',bit)
