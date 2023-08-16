import collections

s='aabbbccde'
st=list(dict(collections.Counter(s)).items())
sd=sorted([((i[1]),i[0]) for i in (sorted(st,reverse=True))],reverse=True)

# for i in (sorted(st,reverse=True)):
#     sd.append((i[1],i[0]))
j=0
for i in range(len(sd)):
    j+=1
    if j==4:
        break
    if sd[i][0]!=sd[i+1][0]:
        print(sd[i][1],sd[i][0])
    elif sd[i][0]==sd[i+1][0]:
        print('%')

        if sd[i][1]>sd[i+1][1]:
            print(sd[i+1][1],sd[i+1][0])
        elif sd[i][1]<sd[i+1][1]:
            
            print(sd[i][1],sd[i][0])
        
print(sd)
