import collections

s='aabbbccde'
st=list(dict(collections.Counter(s)).items())
sd=sorted([((i[1]),i[0]) for i in (sorted(st,reverse=True))],reverse=True)

# for i in (sorted(st,reverse=True)):
#     sd.append((i[1],i[0]))

'''j=1
d={}
for i in range(len(sd)):
    
    if j==4:
        break
    if sd[i][0]!=sd[i+1][0]:
        #print(sd[i][1],sd[i][0])
        d[j]=(sd[i][1],sd[i][0])

    elif sd[i][0]==sd[i+1][0]:
        

        if sd[i][1]>sd[i+1][1]:
            #print(sd[i+1][1],sd[i+1][0])
            d[j+1]=(sd[i][1],sd[i][0])
            d[j]=(sd[i+1][1],sd[i+1][0])
            j+=1

        #elif sd[i][1]<sd[i+1][1]:
            
            #print(sd[i][1],sd[i][0])
    j+=1
        
for i in sorted(d):
    print(d[i][0],d[i][1])'''

        # --------------------------> def a fun reccurion
'''f=[]
def check(ele,l):
    top=ele
    print('#',top)
    if len(l)==0:
        f.append(top)
        print('returned')
        return
    for i in range(len(l)):
        if top[0]==l[i][0]:
            
            if top[1]>l[i][1]:
                print(l[i])
                check(l.pop(i),l)
            
                
            elif top[1]<l[i][1]:
                f.append(top)


j=0
for i in range(3):
    print(i)
    print(f)
    
    for z in f:
        if z in sd:
            sd.remove(z)
    print(sd)
    # print(sd[j])  (1,'z'),(1,'y'),(1,'x')
    
    check(sd.pop(j),sd.copy())
    j+=1
    continue'''

m=[0]*26
print(m)


for i in s:
    m[ord(i)-97]+=1
print(m)

for i in range(3):
    c=m.index(max(m))
    print(c)

    

    print(chr(c+97),max(m))
    m[c]=0
