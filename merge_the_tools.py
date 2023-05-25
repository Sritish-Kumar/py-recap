# merge tools 
# add your string and a number to split it. 
# get the splitted strings without any repetaion of elements/character
# eg. 'AABCAAADA' and 3 ------> output- AB CA AD 

s,k=input('string: ').strip().lower(),int(input('number: '))

for i in range(0,len(s),k):
    r=s[i:i+k]
    
    rx=''
    for j in range(len(r)):
        
        if r[j] not in rx:
            rx+=r[j]
    print(rx)

        
