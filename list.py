N = int(input().strip())
lis=[]

def insert(x):
    y=x.split('insert')
    y1=y[1].strip().split(' ')
    lis.insert(int(y1[0]),int(y1[1]))
def remove(x):
    y=x.split('remove')
    
    lis.remove(int(y[1].strip()))
def append(x):
    y=x.split('append')
    lis.append(int(y[1].strip()))


for i in range(0,N):
    x=input().strip().lower()
    

    if 'insert' in x:
        insert(x)
    elif 'print' in x:
        print(lis)
    elif 'remove' in x:
        remove(x)
    elif 'append' in x:
        append(x)
    elif 'sort' in x:
        lis.sort()
    elif 'pop' in x:
        lis.pop()
    elif 'reverse' in x:
        lis = lis[::-1]
        

    


        
        