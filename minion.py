# this particular code lacks a lot of things
# it failed 10 out of 15 test on hacker rank (runtime error)
# I would really appreciate if anybody could try and mold this so that it can pass all the tests.
#------------ IGNORE THE CAPITAL OUTPUT




print(' - - minion game - -\n')
v='AEIOU'
s=input().strip().upper()#'BANANA'

st={}
ke={}

r=1
def score():
    s=0
    for i in st:
        s+=st[i]
    k=0
    for i in ke:
        k+=ke[i]
    
    if k > s:
        return 'KEVIN',str(k)
    elif k==s:
        return 'DRAW',
    else:
        return 'STUART',str(s)
    


                                # stuart ------> consonant
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

                            # kevin -------------->  vowels
        if s[i] in v:

            if len(s[i:i+r])!=r:
                continue

            if (s[i:i+r]) not in ke:
                ke[s[i:i+r]]=1
            else:
                ke[s[i:i+r]]+=1
        
    r+=1
    if  r==len(s)+1:
        break
    



result= score()
print(' '.join(result))



