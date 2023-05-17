d={1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
n=int(input())


bit=4*n-3
t=2*n-1
od=[i for i in range(1,2*n,2)]
for i in range(0,t):
    if i<(t/2)-1:
        for j in range(od[i]):
            print(d[n].centre(bit,'-'))


print('bit:',bit)
print(od)

