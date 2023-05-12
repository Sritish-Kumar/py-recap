#1) swap case

'''def swap_case(s):
    x=list(s)
    y=[i.upper() if i.islower()==True else i.lower() for i in x]
    z=''
    for i in y:
        z+=i

    return 

        
s = input().strip()
result = swap_case(s)
print(result)'''


#2) string index 


def count_substring(string, sub_string):
    s=len(sub_string)
    count=0
    for i in range(0,len(string)):
        if string[i:i+s]==sub_string:

            count+=1
        elif i == len(string)+1-s+1:
            break

    return count

string = input().strip()
sub_string = input().strip()
        
count = count_substring(string, sub_string)
print(count)
