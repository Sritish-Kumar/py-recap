def wrap(string, max_width):
    l=""
    for i in range(0,len(string),max_width):
        l=l+string[i:i+max_width]+'\n'
    print(l)
    



string, max_width = input().strip(), int(input())
wrap(string, max_width)

