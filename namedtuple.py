# This can be done in a less than 10 lines without using any namedtuple. 
# since i was learning about namedtuple i wrote this. and there is no need to make another function to declare the namedtuple too. 
# you can easily reduce the number of lines in this one. 

import collections

n=int(input())      #NUMBER OF STUDENTS

su=0
def init(l):
    global student
    student=collections.namedtuple('student',l)

for i in range(n):
    if i==0:
        s=input().split()
        init(s)
        
    
    st=input().split()
    s1=student._make(st)
    su+=int(s1.MARKS)

    print(su/n)    #AVERAGE