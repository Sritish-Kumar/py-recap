# finding out the captions room from a list of all rooms
# this code has 2 different versions the 1st one is the long it is not efficient but does the work for small numbers
# the second one is more of a efficient approach and works on all condition. 
# If you have any other render of it please leave it in here to help others too. 

n=int(input()) #5
s=sorted(list(map(int,input().split()))) #[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8]
rx=set(s)
k=(len(s)-1)/n # no. of total groups

# -----------------------> version 1
def cut(i):
    s.remove(i)
    try:
        r=s.index(i)
        return
        print('found',i)
    except:
        print(i)


for i in rx:
    cut(i)

# ---------------------> version 2

'''a=int((5*sum(rx)-sum(s))/(n-1))
print(a)'''
