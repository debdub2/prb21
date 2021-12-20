def rplcstrg(strg, l):
    x = 0
    while x < l-1:
        if strg[x] == "B" and strg[x+1] == "G": 
            strg = strg[:x] + "G" + strg[x+1:]
            strg = strg[:x+1] + "B" + strg[x+2:]
            x += 2
        else:
            x += 2
    return(strg)

if __name__ == '__main__':
    n, t = map(int, input().split())
    s = input()
    for i in range(t):
        s = rplcstrg(s, n)
    print(s)
