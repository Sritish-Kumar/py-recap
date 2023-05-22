'''#s='q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'
s='hello world'
st=[]
for i in range(len(s)):
    if i==len(s)-1:
        st.append(s[i])
    elif s[i+1]==' ' and s[i]!=' ':
        st.append(s[i:i+2])
    elif s[i]==' ' and s[i+1]!=' ':
        continue
    elif s[i]==' ' and s[i+1]==' ':
        st.append(' ')
print(s)   
rx=list(map(str.capitalize,st))
print(''.join(rx))'''

coding_journey = "I love   coding"

coding_journey_split = coding_journey.split(' ',1)

print(coding_journey_split)

# output
# ['I', 'love', '', '', 'coding']