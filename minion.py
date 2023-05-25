print('minion game\n')
v='aeiou'
s='banana'

st={}
r=1
def score():
    s=0
    for i in st:
        s+=st[i]
    return s


                                # stuart - ----> consonant
while True:
    
    for i in range(len(s)):
        if s[i] not in v:

            if len(s[i:i+r])!=r:
                continue
            #print(s[i:i+r],'consonant')
            
            if (s[i:i+r]) not in st:
                st[s[i:i+r]]=1
            else:
                st[s[i:i+r]]+=1
    r+=1
    if  r==len(s)+1:
        break
    

result= score()
print(result)



