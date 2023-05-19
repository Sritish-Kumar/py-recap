'''def print_formatted(number):
    pad = number.bit_length()
    for i in range(1,number+1):
        print(str(i).rjust(pad),oct(i).split("o")[1].rjust(pad),hex(i).split("x")[1].upper().rjust(pad),bin(i).split("b")[1].rjust(pad))

        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)'''

# ------------------     my version
n=int(input())
bit=len(bin(n)[2:])

for i in range(1,n+1):
    print(str(i).rjust(bit,' '),oct(i)[2:].rjust(bit,' '),hex(i).upper()[2:].rjust(bit,' '),bin(i)[2:].rjust(bit,' '))