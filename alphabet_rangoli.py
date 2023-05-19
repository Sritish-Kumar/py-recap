# ALPHABET RANGOLI
# N=int. if n=3 then it would make a rangoli with the 3rd letter "c" as its sides. 
# i would really appreciate if you have any other interation of this rangoli.

d='abcdefghijklmnopqrstuvwxyz'
n=int(input())
n1=n-2    # top side left
n2=0      # top side right

n3=1      # bottom right + left

bit=4*n-3   #length
t=2*n-1     #breadth



for i in range(0,t):

    if i<(t-1)/2:                          #top
        s=d[n-1:n1:-1]+d[n-n2:n]
        st='-'.join(x for x in s)
        print(st.center(bit,'-'))
        n1-=1
        n2+=1


    elif i==(t-1)/2:                       # middle
       
        s=d[n-1::-1]+d[1:n]
        st='-'.join(x for x in s)
        print(st.center(bit,'-'))


    elif i>(t-1)/2:
    
                                           # bottom 
        s=d[n-1:n3:-1]+d[n3:n]
        st='-'.join(x for x in s)
        print(st.center(bit,'-'))
        n3+=1

            


